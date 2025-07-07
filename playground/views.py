# views.py
from django.shortcuts import render
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load once (global)
tokenizer = AutoTokenizer.from_pretrained("allenai/scibert_scivocab_uncased")
model = AutoModelForSequenceClassification.from_pretrained("allenai/scibert_scivocab_uncased", num_labels=2)

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.softmax(logits, dim=1)
    label = torch.argmax(probs).item()
    confidence = probs[0][label].item()
    return ("Fake" if label == 1 else "Real", confidence)

def analyze(request):
    if request.method == "POST":
        input_text = request.POST.get("input_text", "")
        label, confidence = predict(input_text)
        return render(request, "output.html", {
            "input_text": input_text,
            "label": label,
            "confidence": round(confidence * 100, 2)
        })
    return render(request, "input.html")
