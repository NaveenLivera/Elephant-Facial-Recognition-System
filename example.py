#!/usr/bin/env python3
"""
Example script demonstrating basic usage of Elephant Face ID & NFT System.

This script shows how to:
1. Initialize the system
2. Process a single image
3. Process multiple images
4. Generate NFTs
5. View results

Usage:
    python example.py
"""

from pathlib import Path
from elephant_face_id_nft import ElephantFaceIDDetailed, ElephantNFTGeneratorDetailed


def example_single_image():
    """Example: Process a single elephant image."""
    print("\n" + "="*60)
    print("EXAMPLE 1: Processing Single Image")
    print("="*60)
    
    # Initialize system
    system = ElephantFaceIDDetailed()
    
    # Process image
    image_path = "path/to/your/elephant.jpg"
    
    if not Path(image_path).exists():
        print(f"\n⚠ Image not found: {image_path}")
        print("Please update the image_path variable with a valid path.")
        return
    
    result = system.process_image(image_path)
    
    if result:
        print(f"\n✓ SUCCESS!")
        print(f"  Elephant ID: {result['unique_id']}")
        print(f"  Status: {'New elephant' if result['is_new'] else 'Matched existing'}")
        if not result['is_new']:
            print(f"  Match confidence: {result['similarity']:.2%}")
    else:
        print("\n✗ FAILED: Could not process image")


def example_batch_processing():
    """Example: Process multiple images in a folder."""
    print("\n" + "="*60)
    print("EXAMPLE 2: Batch Processing")
    print("="*60)
    
    # Initialize system with dataset path
    dataset_path = "./elephant_images"
    
    if not Path(dataset_path).exists():
        print(f"\n⚠ Dataset folder not found: {dataset_path}")
        print("Creating sample directory...")
        Path(dataset_path).mkdir(exist_ok=True)
        print(f"Please add elephant images to: {dataset_path}")
        return
    
    system = ElephantFaceIDDetailed(dataset_path=dataset_path)
    
    # Process all images
    results = system.process_dataset()
    
    # Display summary
    print(f"\n✓ BATCH PROCESSING COMPLETE!")
    print(f"  Images processed: {len(results)}")
    print(f"  Unique elephants: {len(system.elephants_db)}")
    
    # Show each elephant
    print("\n  Identified Elephants:")
    for i, elephant_id in enumerate(system.elephants_db.keys(), 1):
        count = len(system.elephants_db[elephant_id])
        print(f"    {i}. {elephant_id} ({count} image{'s' if count > 1 else ''})")


def example_nft_generation():
    """Example: Generate NFTs for identified elephants."""
    print("\n" + "="*60)
    print("EXAMPLE 3: NFT Generation")
    print("="*60)
    
    # First, identify some elephants
    system = ElephantFaceIDDetailed(dataset_path="./elephant_images")
    results = system.process_dataset()
    
    if not system.elephants_db:
        print("\n⚠ No elephants in database. Process some images first!")
        return
    
    # Initialize NFT generator
    nft_gen = ElephantNFTGeneratorDetailed()
    
    # Generate NFT for each elephant
    print(f"\nGenerating NFTs for {len(system.elephants_db)} elephants...")
    
    nft_results = []
    for elephant_id in system.elephants_db.keys():
        nft_info = nft_gen.generate_nft_from_elephant_id(elephant_id)
        nft_results.append(nft_info)
        print(f"  ✓ NFT created for {elephant_id}")
    
    print(f"\n✓ NFT GENERATION COMPLETE!")
    print(f"  NFTs created: {len(nft_results)}")
    print(f"  Output directory: {nft_gen.nft_output_dir}")
    print(f"  Images: {nft_gen.images_dir}")
    print(f"  Metadata: {nft_gen.metadata_dir}")


def example_custom_configuration():
    """Example: Using custom configuration."""
    print("\n" + "="*60)
    print("EXAMPLE 4: Custom Configuration")
    print("="*60)
    
    # Custom model directory
    system = ElephantFaceIDDetailed(
        model_dir="./my_models",
        dataset_path="./elephant_images"
    )
    
    # Adjust match threshold for stricter matching
    system.match_threshold = 0.65  # Default is 0.55
    print(f"\n✓ Match threshold set to: {system.match_threshold}")
    
    # Process with custom settings
    image_path = "path/to/elephant.jpg"
    if Path(image_path).exists():
        result = system.process_image(image_path)
        print(f"  Processed with custom threshold")


def example_database_inspection():
    """Example: Inspect the elephant database."""
    print("\n" + "="*60)
    print("EXAMPLE 5: Database Inspection")
    print("="*60)
    
    # Load system
    system = ElephantFaceIDDetailed()
    
    if not system.elephants_db:
        print("\n⚠ Database is empty. Process some images first!")
        return
    
    # Database statistics
    total_elephants = len(system.elephants_db)
    total_embeddings = sum(len(embs) for embs in system.elephants_db.values())
    avg_embeddings = total_embeddings / total_elephants if total_elephants > 0 else 0
    
    print(f"\n📊 DATABASE STATISTICS:")
    print(f"  Total elephants: {total_elephants}")
    print(f"  Total embeddings: {total_embeddings}")
    print(f"  Average embeddings per elephant: {avg_embeddings:.1f}")
    
    # Show details for each elephant
    print(f"\n🐘 ELEPHANT DETAILS:")
    for elephant_id, embeddings in system.elephants_db.items():
        print(f"  • {elephant_id}")
        print(f"    - Embeddings: {len(embeddings)}")
        print(f"    - Embedding dimension: {embeddings[0].shape}")


def main():
    """Run all examples."""
    print("\n" + "="*60)
    print("ELEPHANT FACE ID & NFT SYSTEM - EXAMPLES")
    print("="*60)
    
    # Choose which examples to run
    examples = {
        "1": ("Single Image Processing", example_single_image),
        "2": ("Batch Processing", example_batch_processing),
        "3": ("NFT Generation", example_nft_generation),
        "4": ("Custom Configuration", example_custom_configuration),
        "5": ("Database Inspection", example_database_inspection),
    }
    
    print("\nAvailable examples:")
    for key, (name, _) in examples.items():
        print(f"  {key}. {name}")
    print("  A. Run all examples")
    print("  Q. Quit")
    
    choice = input("\nSelect an example (1-5, A, Q): ").strip().upper()
    
    if choice == "Q":
        print("\nGoodbye!")
        return
    elif choice == "A":
        # Run all examples
        for name, func in examples.values():
            try:
                func()
            except Exception as e:
                print(f"\n✗ Error in {name}: {str(e)}")
    elif choice in examples:
        # Run selected example
        name, func = examples[choice]
        try:
            func()
        except Exception as e:
            print(f"\n✗ Error: {str(e)}")
    else:
        print("\n⚠ Invalid choice!")
    
    print("\n" + "="*60)
    print("Examples completed!")
    print("="*60)


if __name__ == "__main__":
    main()
