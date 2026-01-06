# export/convert_to_gguf.py

from unsloth import FastLanguageModel
import os

# Define path to your fine-tuned checkpoint or base model
# If you just finished training in the notebook, 'model' is already in memory.
# If reloading:
# model, tokenizer = FastLanguageModel.from_pretrained("outputs/checkpoint-60", ...)

def export_model(model, tokenizer, output_format="q4_k_m"):
    """
    Exports the model to GGUF format for llama.cpp/mobile execution.
    
    Args:
        output_format (str): The quantization method. 
                             'q4_k_m' is recommended for balance of size/perf.
                             'q8_0' is higher precision but larger size.
    """
    print(f"Starting export to GGUF format: {output_format}...")
    
    # Save to GGUF
    model.save_pretrained_gguf(
        "model_export", 
        tokenizer, 
        quantization_method = output_format
    )
    
    print(f"Export complete. File saved in 'model_export/' directory.")

if __name__ == "__main__":
    # This assumes this script is run where 'model' and 'tokenizer' are available
    # or you load them here.
    pass
