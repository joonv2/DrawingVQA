import json
import hashlib
from datasets import Dataset, Features, Value, Sequence

# ============================================================
# STEP 1: CONFIGURATION — Edit these values
# ============================================================

HF_USERNAME  = "S2-MIND"
DATASET_NAME = "DrawingVQA"
REPO_ID      = f"{HF_USERNAME}/{DATASET_NAME}"

# Path to your JSON file (list of question objects)
DATA_FILE = "huggingface/00_DrawingVQA_data.json"


# ============================================================
# STEP 2: LOAD YOUR DATA
#
# Your JSON is a list of objects. Each object has nested fields
# like "options" (a dict) and "cv_field" (a list). We load the
# raw JSON directly — no need for pandas since it's not tabular.
# ============================================================

print("Loading data...")
with open(DATA_FILE, "r") as f:
    raw_data = json.load(f)

print(f"  Loaded {len(raw_data)} records")

# ============================================================
# STEP 3: FLATTEN / NORMALIZE
#
# HuggingFace datasets work best with flat, typed columns.
# The "options" dict (A/B/C/D) is nested — we flatten it into
# separate columns (option_a, option_b, ...) so each cell is a
# plain string. This makes the dataset easier to use downstream.
#
# "cv_field" is a list (multi-label), so we keep it as-is —
# HuggingFace supports Sequence(Value("string")) for list columns.
# ============================================================

def hash_name(name):
    # Create a unique hash of the name to avoid public from seeing the original name. Use this for any contents / fields that require it. 
    if name is None:
        return None
    return hashlib.sha256(name.encode()).hexdigest()[:16]

def as_list(value):
    # If already a list, return as-is.
    # If a bare string, wrap it — avoids Python iterating chars ("ocr" → ["o","c","r"]).
    # If None/missing, return empty list.
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]

def normalize(record):
    options = record.get("options") or {}
    # If options was stored as a JSON string instead of a dict, parse it
    if isinstance(options, str):
        if options.strip():
            try:
                options = json.loads(options)
            except json.JSONDecodeError:
                print(f"  WARNING: could not parse options value: {repr(options)}")
                options = {}
        else:
            options = {}
    return {
        "image_name":       hash_name(record.get("image_name")),
        "image2_name":      hash_name(record.get("image2_name")),
        "question":         record.get("question"),
        # Flatten the options dict into individual columns
        "option_a":         options.get("A"),
        "option_b":         options.get("B"),
        "option_c":         options.get("C"),
        "option_d":         options.get("D"),
        "answer":           record.get("answer"),
        "explanation":      record.get("explanation"),
        # These are all list fields — wrap bare strings to avoid char-iteration
        "cv_field":         as_list(record.get("cv_field")),
        "cv_subfield":      as_list(record.get("cv_subfield")),
        "ce_field":         as_list(record.get("ce_field")),
        "ce_subfield":      as_list(record.get("ce_subfield")),
        "topic_difficulty": record.get("topic_difficulty"),
        "question_type":    record.get("question_type"),
    }

# Preserve the hash mapping structure just in case. 
mapping = {
    r["image_name"]: hash_name(r["image_name"]) for r in raw_data if r.get("image_name")
}

with open("00_private_image_name_mapping.json", "w") as f:
    json.dump(mapping, f, indent=2)
print("  Saved private image name mapping to 00_private_image_name_mapping.json")

print("Normalizing records...")
normalized = [normalize(r) for r in raw_data]


# ============================================================
# STEP 4: DEFINE THE SCHEMA (Features)
#
# Explicitly declaring features tells HuggingFace the exact type
# of each column. Without this, it infers types and can get them
# wrong (e.g. treating a nullable string as a null column).
#
# Value("string") = a single nullable string
# Sequence(Value("string")) = a list of strings (for cv_field)
# ============================================================

features = Features({
    "image_name":       Value("string"),
    "image2_name":      Value("string"),
    "question":         Value("string"),
    "option_a":         Value("string"),
    "option_b":         Value("string"),
    "option_c":         Value("string"),
    "option_d":         Value("string"),
    "answer":           Value("string"),
    "explanation":      Value("string"),
    "cv_field":         Sequence(Value("string")),
    "cv_subfield":      Sequence(Value("string")),
    "ce_field":         Sequence(Value("string")),
    "ce_subfield":      Sequence(Value("string")),
    "topic_difficulty": Value("string"),
    "question_type":    Value("string"),
})


# ============================================================
# STEP 5: CONVERT TO HUGGING FACE DATASET FORMAT
#
# Dataset.from_list() takes a list of dicts — one dict per row.
# We pass our features schema so types are enforced at load time.
# ============================================================

print("\nConverting to HF Dataset format...")

# Reformat from list-of-dicts to dict-of-lists (required by from_dict)
columns = {key: [r[key] for r in normalized] for key in normalized[0]}
dataset = Dataset.from_dict(columns, features=features)
print(dataset)


# ============================================================
# STEP 6: PREVIEW BEFORE UPLOADING
# ============================================================

print("\nFirst 3 records:")
for i in range(min(3, len(dataset))):
    print(dataset[i])


# ============================================================
# STEP 7: UPLOAD TO HUGGING FACE
# ============================================================

print(f"\nUploading to HF Hub as: {REPO_ID}")

dataset.push_to_hub(
    REPO_ID,
    split="benchmark",
    private=True,   # Set to False if you want it public
)

print("\nDone! View your dataset at:")
print(f"  https://huggingface.co/datasets/{REPO_ID}")
