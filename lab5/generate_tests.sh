#!/bin/bash

# Set the base directory ,you can set the below paths as your file paths
BASE_DIR="/home/set-iitgn-vm/lab5/algorithms"
ALGORITHMS_DIR="$BASE_DIR/algorithms"
OUTPUT_DIR="$BASE_DIR/generated_tests"

# Create output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

# Find all .py files in the algorithms directory (excluding _init_.py)
find $ALGORITHMS_DIR -name "*.py" | grep -v "_init_.py" | sort | while read -r file; do
    # Convert file path to module name
    # Remove base dir and .py extension
    rel_path=${file#$BASE_DIR/}
    module_name=${rel_path%.py}
    # Replace / with .
    module_name=${module_name//\//.}
    
    # Create the output directory
    module_output_dir="$OUTPUT_DIR/${module_name}"
    mkdir -p "$module_output_dir"
    
    echo "Generating tests for module: $module_name"
    # Run Pynguin
    PYNGUIN_DANGER_AWARE=1 pynguin --project-path "$BASE_DIR" --module-name "$module_name" --output-path "$module_output_dir"
done

echo "Test generation complete!"
