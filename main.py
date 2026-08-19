from hr_assistant.pipeline import ask, build_hr_assistant
from hr_assistant.logger import get_logger

logger= get_logger(__name__)
def main():
    logger.info("===CLI RUN Started===")
    agent= build_hr_assistant()
    demo_questions= [
        "How  many paid annual leave do i get?",
        "What is the notice period during probation?",
        "Can i work from home every day?"
    ]
    for question in demo_questions:
        print("=" * 60)
        print("QUESTION:", question)
        print("-" * 60)
        answer =  ask(agent,question)
        print("ANSWER:", answer)
        print("=" * 60)
        print()

        logger.info("=== CLI run finished ====")

if __name__ == "__main__":
    main()
