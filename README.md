# **Universal LLM-based OCR (Image → Text Extraction)**

This project demonstrates how to perform **OCR (Optical Character Recognition)** using **any Large Language Model (LLM)** that supports image input via the **OpenAI-compatible SDK** (OpenAI, OpenRouter, Groq, Together, etc.).

It works with models such as:

* GPT-4o / GPT-4o-mini
* Llama Vision models
* Claude Vision (via OpenAI-compatible routers)
* Any future LLM that accepts `"image_url"` or `"image_base64"`

---

## 🚀 **Features**

* **LLM-powered OCR (not traditional Tesseract OCR)**
* Works with **any model endpoint** that accepts images
* **Supports:**

  * 🌐 Image URLs
  * 🖼️ Local images (converted to Base64)
* **Preserves structure & formatting**
* Output can be printed or saved to a text file
* Easily extendable to:

  * JSON output
  * Multi-image extraction
  * PDF → Image → Text pipelines

---

## 📦 **Requirements**

* Python 3.8+
* `openai` (or compatible OpenRouter SDK)
* `base64` (comes with Python)

Install dependencies:

```bash
pip install openai python-dotenv
```

---

## ⚙️ **Configuration**

Set up your API key:

```python
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)
```

You can replace the base URL or model with **any LLM endpoint**.

---

## 🧠 **Why LLM-based OCR?**

Unlike classical OCR tools (Tesseract, EasyOCR), LLMs:

* Understand complex layouts
* Extract text from low-quality images
* Preserve meaning, structure, labels
* Interpret tables, paragraphs, and mixed fonts

This project shows how to use LLMs as intelligent OCR engines.

---

## 🧰 **Usage**

### ✔️ **Extract Text from an Image URL**

```python
image_url = "https://example.com/image.jpg"
extracted_text = image_to_text_from_url(image_url)

with open("output.txt", "a", encoding="utf-8") as f:
    f.write(extracted_text)
```

---

### ✔️ **Extract Text from a Local Image**

```python
local_image_path = "image.png"
image_base64 = image_to_base64(local_image_path)

text = image_to_text_from_base64(image_base64)
print(text)
```

---

## 🗂️ **Functions Overview**

### **`image_to_base64(image_path)`**

Converts local image → Base64 string.

### **`image_to_text_from_url(image_url)`**

Sends URL directly to the LLM and extracts text.

### **`image_to_text_from_base64(image_base64)`**

Sends Base64-encoded image to the LLM vision endpoint.

---

## 🔄 **Model-Agnostic Design**

Just change one line:

```python
model="gpt-4o-mini"
```

to:

```python
model="llama-3.2-vision"
# or
model="gpt-4o"
# or
model="groq-vision-preview"
# or
model="any-supported-model"
```

No other code changes needed!

---

## 📌 **Use Cases**

* Invoice/receipt text extraction
* Handwritten notes to digital text
* OCR for PDFs (after converting PDF → image)
* Dataset preparation
* Document summarization via OCR

---

## 🤝 Contributing

Issues and pull requests are welcome.
You can extend this to PDF OCR, batch processing, or JSON structured output.

---

## 📄 License

MIT License — free to use and modify.
