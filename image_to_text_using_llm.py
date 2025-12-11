from openai import OpenAI
import base64
# import requests

# Initialize OpenAI client with API key
client = OpenAI(
    api_key="your-openai-api-key"
    )

def image_to_base64(image_path):
    """Converts a local image to a base64 encoded string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def image_to_text_from_url(image_url):
    """Extracts text from an image using its URL."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Extract all the text content from this image."},
                    {"type": "image_url", "image_url": {"url": image_url}},
                ],
            }
        ],
        max_tokens=300,
    )
    return response.choices[0].message.content

def image_to_text_from_base64(image_base64):
    """Extracts text from an image using its base64 encoding."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Extract all the text content from this image thoroughly and accurately. Ensure that no lines, words, or parts of the content are missed, even if the text is faint, small, or near the edges. The text may include headings, paragraphs, or lists and could appear in various fonts, styles, or layouts. Carefully preserve the reading order and structure as it appears in the image. Double-check for any skipped lines or incomplete content, and extract every visible text element, ensuring completeness across all sections. This is crucial for the task's accuracy."
                        )
                    },
                    {"type": "image_url", "image_url": {
                        "url": f"data:image/png;base64,{image_base64}"}
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    return response.choices[0].message.content

# Example usage:
if __name__ == "__main__":
    # Example 1: Using an image URL
    # image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
    # print("Extracted text from URL:")
    # extracted_text = image_to_text_from_url(image_url)
    # output_file_path = "path/to/extracted_text.txt"
    # with open(output_file_path, "a", encoding="utf-8") as text_file:
    #     text_file.write(extracted_text)
    #     text_file.write("\n")

    # Example 2: Using a base64 encoded image
    local_image_path = "path/to/image.png"  # Replace with your local image path
    image_base64 = image_to_base64(local_image_path)
    print("\nExtracted text from Base64:")
    extracted_text = image_to_text_from_base64(image_base64)
    print(extracted_text)
    output_file_path = "path/to/extracted_text.txt"
    with open(output_file_path, "w", encoding="utf-8") as text_file:
        text_file.write(extracted_text)
        text_file.write("\n")
