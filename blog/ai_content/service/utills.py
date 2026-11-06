from ..client import ContentClient

def validate_text_input(text:str,min_length: int=20 , field_name:str ="Content") -> str:

    if not text or not text.strip():
        raise ValueError(f"{field_name}cannot be empty or whitespace.")

    cleand_text = text.strip()
    if len(cleand_text) < min_length:
        raise ValueError(f"{field_name} must be at least {min_length} characters long.")
    return cleand_text

def validate_title(title: str, min_length: int = 5)-> str:

    return validate_text_input(title, min_length, field_name="Title")

def generate_ai_content(prompt: str, system: str = None)-> str:
    client = ContentClient()
    result = client.generate(prompt, system=system)
    print("result",result)

    cleand_result = result.strip()

    print("cleand_result",cleand_result)
    if not cleand_result:
        raise ValueError("Model output was empty or invalid.")

    return cleand_result