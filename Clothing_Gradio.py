import os
from functools import lru_cache

import gradio as gr
import google.generativeai as genai


APP_TITLE = "StyleMe AI"
APP_SUBTITLE = (
    "Personalized outfit recommendations powered by Google Gemini. "
    "Describe your body shape, height, and size to get practical styling guidance."
)
MODEL_NAME = "gemini-2.5-flash"

def get_api_key() -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set")
    return api_key


@lru_cache(maxsize=1)
def get_model() -> genai.GenerativeModel:
    genai.configure(api_key=get_api_key())
    return genai.GenerativeModel(MODEL_NAME)


def build_prompt(body_shape: str, height: str, gender: str, size: str) -> str:
    return (
        "You are an expert fashion stylist. Give concise, practical, and personalized "
        "outfit advice for a user with the following profile:\n\n"
        f"- Gender: {gender}\n"
        f"- Body shape: {body_shape}\n"
        f"- Height: {height}\n"
        f"- Clothing size: {size}\n\n"
        "Respond with these sections:\n"
        "1. Best outfit ideas\n"
        "2. Fit and silhouette tips\n"
        "3. Color and pattern suggestions\n"
        "4. One quick styling tip\n\n"
        "Keep the advice respectful, fashion-focused, and easy to apply in daily life."
    )

def recommend_clothes(body_shape, height, gender, size):
    if not all([body_shape, height, gender, size]):
        return "Please fill in all fields before generating recommendations."

    prompt = build_prompt(body_shape, height, gender, size)
    try:
        response = get_model().generate_content(prompt)
        if response and response.text:
            return response.text.strip()
        return "The model returned no recommendations. Please try again."
    except Exception as e:
        return f"Unable to generate recommendations right now: {str(e)}"


# Theme CSS with light and dark mode support
css = """
:root {
    --bg-primary: #f8fafc;
    --bg-secondary: #f1f5f9;
    --bg-tertiary: white;
    --text-primary: #0f172a;
    --text-secondary: #334155;
    --border-color: #e2e8f0;
    --shadow-color: rgba(15, 23, 42, 0.05);
    --hero-bg-1: #1e293b;
    --hero-bg-2: #0f172a;
    --accent-1: #fbbf24;
    --accent-2: #f59e0b;
    --button-bg-1: #3b82f6;
    --button-bg-2: #2563eb;
    --button-shadow: rgba(59, 130, 246, 0.3);
}

@media (prefers-color-scheme: dark) {
    :root {
        --bg-primary: #0f172a;
        --bg-secondary: #1e293b;
        --bg-tertiary: #1e293b;
        --text-primary: #f8fafc;
        --text-secondary: #cbd5e1;
        --border-color: #334155;
        --shadow-color: rgba(0, 0, 0, 0.3);
        --hero-bg-1: #0f172a;
        --hero-bg-2: #000000;
        --accent-1: #fcd34d;
        --accent-2: #fbbf24;
        --button-bg-1: #3b82f6;
        --button-bg-2: #1d4ed8;
        --button-shadow: rgba(59, 130, 246, 0.5);
    }
}

html[data-theme="dark"] {
    --bg-primary: #0f172a;
    --bg-secondary: #1e293b;
    --bg-tertiary: #1e293b;
    --text-primary: #f8fafc;
    --text-secondary: #cbd5e1;
    --border-color: #334155;
    --shadow-color: rgba(0, 0, 0, 0.3);
    --hero-bg-1: #0f172a;
    --hero-bg-2: #000000;
    --accent-1: #fcd34d;
    --accent-2: #fbbf24;
    --button-bg-1: #3b82f6;
    --button-bg-2: #1d4ed8;
    --button-shadow: rgba(59, 130, 246, 0.5);
}

html[data-theme="light"] {
    --bg-primary: #f8fafc;
    --bg-secondary: #f1f5f9;
    --bg-tertiary: white;
    --text-primary: #0f172a;
    --text-secondary: #334155;
    --border-color: #e2e8f0;
    --shadow-color: rgba(15, 23, 42, 0.05);
    --hero-bg-1: #1e293b;
    --hero-bg-2: #0f172a;
    --accent-1: #fbbf24;
    --accent-2: #f59e0b;
    --button-bg-1: #3b82f6;
    --button-bg-2: #2563eb;
    --button-shadow: rgba(59, 130, 246, 0.3);
}

body, .gradio-container {
    background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
    color: var(--text-primary);
}

.gradio-container {
    max-width: 1200px !important;
    padding-top: 24px !important;
    padding-bottom: 32px !important;
}

.theme-toggle {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    margin-bottom: 16px;
    border-radius: 10px;
    background: var(--bg-tertiary);
    border: 1px solid var(--border-color);
    font-size: 0.9rem;
    color: var(--text-secondary);
}

.hero {
    padding: 40px 32px;
    border-radius: 20px;
    background: linear-gradient(135deg, var(--hero-bg-1) 0%, var(--hero-bg-2) 100%);
    color: white;
    box-shadow: 0 20px 50px var(--shadow-color);
    margin-bottom: 32px;
    border: 1px solid rgba(51, 65, 85, 0.5);
}

.hero h1 {
    margin: 0 0 12px 0;
    font-size: 2.2rem;
    font-weight: 700;
    background: linear-gradient(135deg, var(--accent-1) 0%, var(--accent-2) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero p {
    margin: 0;
    font-size: 1rem;
    line-height: 1.6;
    color: rgba(255, 255, 255, 0.9);
    font-weight: 400;
}

.input-panel {
    padding: 28px;
    border-radius: 16px;
    background: var(--bg-tertiary);
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 12px var(--shadow-color);
}

.output-panel {
    padding: 28px;
    border-radius: 16px;
    background: var(--bg-tertiary);
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 12px var(--shadow-color);
}

.section-header {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 16px;
}

.gradio-form {
    gap: 16px !important;
}

.gr-button {
    border-radius: 12px !important;
    font-weight: 600 !important;
    padding: 12px 24px !important;
}

.gr-button-primary {
    background: linear-gradient(135deg, var(--button-bg-1) 0%, var(--button-bg-2) 100%) !important;
    border: none !important;
    box-shadow: 0 4px 12px var(--button-shadow) !important;
    color: white !important;
}

.gr-button-primary:hover {
    box-shadow: 0 6px 20px var(--button-shadow) !important;
}

.gr-textbox, .gr-dropdown {
    border-radius: 10px !important;
    border: 1.5px solid var(--border-color) !important;
    background: var(--bg-tertiary) !important;
    color: var(--text-primary) !important;
}

.gr-textbox:focus, .gr-dropdown:focus {
    border-color: var(--button-bg-1) !important;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
}

.gr-markdown {
    line-height: 1.8;
    color: var(--text-secondary);
}

.gr-markdown h3 {
    color: var(--text-primary);
    font-size: 1.05rem;
    margin-bottom: 8px;
}

.gr-dropdown-menu, .gr-dropdown-list {
    background: var(--bg-tertiary) !important;
    color: var(--text-primary) !important;
    border-color: var(--border-color) !important;
}

.gr-dropdown-item:hover {
    background: var(--bg-secondary) !important;
}
"""

with gr.Blocks() as demo:
    gr.Markdown(
        """<script>
        function toggleTheme() {
            const html = document.documentElement;
            const currentTheme = html.getAttribute('data-theme') || 'light';
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            html.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            location.reload();
        }
        
        // Apply saved theme on load
        window.addEventListener('load', function() {
            const savedTheme = localStorage.getItem('theme') || 'light';
            document.documentElement.setAttribute('data-theme', savedTheme);
        });
        </script>"""
    )
    
    gr.Markdown(
        f"""
        <div class="hero">
            <h1>{APP_TITLE}</h1>
            <p>{APP_SUBTITLE}</p>
        </div>
        """
    )
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("")
        with gr.Column(scale=1, min_width=120):
            gr.HTML("""
                <div style="text-align: right; margin-top: 12px;">
                    <button onclick="toggleTheme()" style="
                        padding: 8px 16px;
                        border-radius: 8px;
                        border: 1px solid #e2e8f0;
                        background: white;
                        cursor: pointer;
                        font-size: 0.9rem;
                        font-weight: 500;
                        transition: all 0.3s;
                    " onmouseover="this.style.background='#f1f5f9'" onmouseout="this.style.background='white'">
                        🌙 Dark Mode
                    </button>
                </div>
            """)

    with gr.Row():
        with gr.Column(scale=1, elem_classes=["input-panel"]):
            gr.Markdown("### 👤 Your Profile", elem_classes=["section-header"])
            gender = gr.Dropdown(["Male", "Female", "Non-binary"], label="Gender", value="Female")
            body_shape = gr.Dropdown(
                ["Hourglass", "Pear", "Rectangle", "Apple", "Inverted Triangle", "Athletic", "Round"],
                label="Body Shape",
                value="Rectangle",
            )
            height = gr.Textbox(label="Height", placeholder="Example: 170 cm or 5'7\"")
            size = gr.Dropdown(["XS", "S", "M", "L", "XL", "XXL"], label="Clothing Size", value="M")
            submit_btn = gr.Button("✨ Generate Recommendations", variant="primary")

        with gr.Column(scale=1, elem_classes=["output-panel"]):
            gr.Markdown("### 👗 Your Recommendations", elem_classes=["section-header"])
            output = gr.Markdown(value="Fill in your profile and click 'Generate Recommendations' to get personalized styling tips.")

    gr.Examples(
        examples=[
            ["Female", "Hourglass", "168 cm", "M"],
            ["Male", "Rectangle", "5'10\"", "L"],
            ["Non-binary", "Pear", "160 cm", "S"],
        ],
        inputs=[gender, body_shape, height, size],
        label="🎯 Try These Examples",
    )

    submit_btn.click(recommend_clothes, inputs=[body_shape, height, gender, size], outputs=output)

if __name__ == "__main__":
    server_port = int(os.getenv("GRADIO_SERVER_PORT", os.getenv("PORT", 7860)))
    demo.launch(server_name="0.0.0.0", server_port=server_port, theme=gr.themes.Soft(), css=css)
