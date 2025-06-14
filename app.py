# app.py
from orchestration import OrchestrationAgent

if __name__ == "__main__":
    orchestrator = OrchestrationAgent()
    topic = "How AI is Transforming Education"
    output = orchestrator.run(topic, tone="informative", language="English")
    for key, value in output.items():
        print(f"\n==== {key.upper()} ====")
        print(value)


# streamlit_ui.py
import streamlit as st
from orchestration import OrchestrationAgent

st.set_page_config(page_title="Multi-Agent Content Crafter", layout="wide")

st.title("🧠 AI Content Generator (ADK Multi-Agent)")
topic = st.text_input("Enter Topic:", "The Impact of Climate Change on Agriculture")
tone = st.selectbox("Select Tone:", ["formal", "informal", "persuasive", "technical"])
language = st.selectbox("Select Language:", ["English", "Hindi", "Spanish", "French"])

if st.button("Generate Content"):
    with st.spinner("Agents at work..."):
        orchestrator = OrchestrationAgent()
        results = orchestrator.run(topic, tone=tone, language=language)

        st.subheader("📝 Plan")
        st.markdown(results["plan"])

        st.subheader("🔍 Research")
        st.markdown(results["research"])

        st.subheader("📄 Generated Content")
        st.markdown(results["content"])

        st.subheader("✍️ Refined Content")
        st.markdown(results["refined_content"])

        st.subheader("💻 Code Snippet")
        st.code(results["code"], language="python")

        st.subheader("🎨 Image Prompt")
        st.markdown(results["image_prompt"])

        st.success("Done!")
