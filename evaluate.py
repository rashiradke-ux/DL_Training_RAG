import json
from pathlib import Path
from rag_pipeline import CollegeRAG

def main():
    docs_dir = Path("test_documents")
    if not docs_dir.exists():
        docs_dir = Path("documents")

    print(f"Loading knowledge base from {docs_dir}...")
    rag = CollegeRAG(docs_dir, min_score=0.08)
    count = rag.ingest()
    print(f"Ingested {count} chunks successfully.\n")

    with open("test_questions.json", "r", encoding="utf-8") as f:
        questions = json.load(f)

    print("=" * 80)
    print(f"{'ID':<4} | {'Scenario':<25} | {'Status':<22} | {'Confidence'}")
    print("=" * 80)

    for item in questions:
        q_id = item["id"]
        scenario = item["scenario"]
        query = item["question"]
        expected = item["expected"]

        result = rag.answer(query)
        status = result["status"]
        conf = result.get("confidence", 0.0)

        print(f"{q_id:<4} | {scenario:<25} | {status:<22} | {conf:.3f}")
        print(f"     Q: {query}")
        print(f"     Expected: {expected}")
        if status == "answered":
            sources = [s["source"] for s in result.get("sources", [])]
            print(f"     Sources: {', '.join(set(sources))}")
        elif status == "conflicting_evidence":
            conflicts = [c["source"] for c in result.get("conflicts", [])]
            print(f"     Conflict detected between: {', '.join(conflicts)}")
        elif status == "insufficient_evidence":
            print("     Result: Abstains properly (no hallucination)")
        print("-" * 80)

if __name__ == "__main__":
    main()

