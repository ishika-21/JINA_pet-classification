from jina import Document, DocumentArray, Flow

   docs = DocumentArray(from_csv(file, field_resolver={"Description": "text"}))
