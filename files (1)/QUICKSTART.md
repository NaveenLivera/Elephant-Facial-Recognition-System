# Quick Start Guide

Get up and running with the Elephant Face ID & NFT System in 5 minutes!

## Installation (2 minutes)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/elephant-face-id-nft.git
cd elephant-face-id-nft
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

That's it! You're ready to go.

## Basic Usage (3 minutes)

### Option 1: Process Single Image

```python
from elephant_face_id_nft import ElephantFaceIDDetailed

# Initialize system
system = ElephantFaceIDDetailed()

# Process one image
result = system.process_image("path/to/elephant.jpg")

# View results
print(f"Elephant ID: {result['unique_id']}")
print(f"Status: {'New' if result['is_new'] else 'Matched'}")
print(f"Confidence: {result['similarity']:.2%}")
```

### Option 2: Process Entire Folder

```python
from elephant_face_id_nft import ElephantFaceIDDetailed

# Initialize with dataset path
system = ElephantFaceIDDetailed(dataset_path="./my_elephant_photos")

# Process all images
results = system.process_dataset()

# View summary
print(f"Processed: {len(results)} images")
print(f"Unique elephants: {len(system.elephants_db)}")
```

### Option 3: Generate NFTs

```python
from elephant_face_id_nft import ElephantNFTGeneratorDetailed

# Initialize NFT generator
nft_gen = ElephantNFTGeneratorDetailed()

# Generate NFT for an elephant
nft_info = nft_gen.generate_nft_from_elephant_id(
    elephant_id="ELE-1234-5678-90ab-cdef"
)

print(f"NFT created: {nft_info['image_path']}")
```

## Prepare Your Data

### Directory Structure

```
my_project/
├── elephant_images/          # Your elephant photos
│   ├── elephant1.jpg
│   ├── elephant2.jpg
│   └── elephant3.jpg
└── elephant_face_id_nft.py   # The main script
```

### Supported Image Formats

- `.jpg` / `.jpeg`
- `.png`
- `.bmp`

### Image Requirements

- **Minimum size**: 224×224 pixels
- **Recommended**: 800×800 or larger
- **Content**: Clear view of elephant face
- **Lighting**: Well-lit images work best

## Understanding the Output

### Console Output

The system provides detailed progress:

```
================================================================================
 PROCESSING IMAGE: elephant1.jpg 
================================================================================
  ✓ File Status: FOUND
  ✓ Image Shape: 1920 x 1080 x 3
  
[STEP 4] Detecting Elephant Face
  ✓ Method 1 Candidates: 1
  ✓ Final Candidates Found: 1

[STEP 9] Extracting All Features
  ✓ Processing Views: 13 augmented views
  ✓ Final Feature Count: 72

================================================================================
 FINAL IDENTIFICATION RESULT 
================================================================================
  ✓ ELEPHANT ID: ELE-a3f2-9c4d-1b7e-8f03
  ✓ STATUS: NEW ELEPHANT
```

### Generated Files

```
elephant_models/
├── elephants_database.pkl    # Database of known elephants
├── pca_features.pkl          # PCA model
└── feature_scaler.pkl        # Feature scaler

thesis_comparisons/
├── face_alignment_normalization/
│   └── 001_elephant1_alignment_comparison.jpg
└── view_augmentation_pose_invariance/
    └── 001_elephant1_augmentation_comparison_grid.jpg

elephant_nfts/
├── images/
│   └── ELE_a3f2_9c4d_1b7e_8f03.jpg
└── metadata/
    └── ELE_a3f2_9c4d_1b7e_8f03_metadata.json
```

## Example: Complete Workflow

```python
# Complete example: Process images and generate NFTs

# 1. Import classes
from elephant_face_id_nft import ElephantFaceIDDetailed, ElephantNFTGeneratorDetailed

# 2. Initialize systems
elephant_system = ElephantFaceIDDetailed(dataset_path="./elephant_photos")
nft_generator = ElephantNFTGeneratorDetailed()

# 3. Process all images
print("Processing elephant images...")
results = elephant_system.process_dataset()

# 4. Generate NFTs for each unique elephant
print("\nGenerating NFTs...")
for elephant_id in elephant_system.elephants_db.keys():
    nft_info = nft_generator.generate_nft_from_elephant_id(elephant_id)
    print(f"✓ NFT created for {elephant_id}")

# 5. Summary
print("\n" + "="*60)
print("COMPLETE!")
print(f"Images processed: {len(results)}")
print(f"Unique elephants: {len(elephant_system.elephants_db)}")
print(f"NFTs generated: {len(elephant_system.elephants_db)}")
print("="*60)
```

## Configuration

### Adjust Match Threshold

```python
# More strict matching (fewer false positives)
system = ElephantFaceIDDetailed()
system.match_threshold = 0.65  # Default: 0.55

# More lenient matching (fewer false negatives)
system.match_threshold = 0.45
```

### Change NFT Size

```python
nft_gen = ElephantNFTGeneratorDetailed()

# Create larger NFT
nft_info = nft_gen.create_nft_image(
    elephant_id="ELE-1234-...",
    width=2048,
    height=2048
)
```

### Custom Output Directory

```python
system = ElephantFaceIDDetailed(model_dir="./my_custom_models")
```

## Troubleshooting

### "No faces detected"

**Solutions:**
- Ensure image shows clear elephant face
- Try different image angles
- Check image quality/resolution
- Adjust lighting/contrast

### Import errors

```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### "Database not found"

This is normal on first run. The system creates a new database automatically.

### Low match confidence

- Collect more reference images for each elephant
- Ensure consistent lighting across images
- Use higher resolution images

## Quick Performance Tips

1. **Use good quality images** (>800×800 pixels)
2. **Consistent lighting** improves matching
3. **Multiple angles** per elephant improve accuracy
4. **Regular database cleanup** with `merge_similar_elephants()`

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
- Explore example notebooks (coming soon)
- Join our community discussions

## Pro Tips

```python
# Tip 1: Process in batches for large datasets
import os
from pathlib import Path

image_dir = Path("./large_dataset")
batch_size = 50

image_files = list(image_dir.glob("*.jpg"))
for i in range(0, len(image_files), batch_size):
    batch = image_files[i:i+batch_size]
    for img in batch:
        system.process_image(img)

# Tip 2: Export database for backup
import pickle

with open("backup_database.pkl", "wb") as f:
    pickle.dump(system.elephants_db, f)

# Tip 3: Get detailed statistics
total_embeddings = sum(len(embs) for embs in system.elephants_db.values())
avg_embeddings = total_embeddings / len(system.elephants_db)
print(f"Average embeddings per elephant: {avg_embeddings:.1f}")
```

## Learning Resources

- **Computer Vision Basics**: Understanding face detection
- **Feature Extraction**: Texture and anatomical features
- **NFT Standards**: ERC-721 and metadata
- **Conservation Technology**: How tech helps wildlife

---

**Need help?** Open an issue on GitHub or check the discussions!

Happy elephant identifying! 
