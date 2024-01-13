import gradio as gr

def dropdown_selection(prefered_professor, prefered_time_range, GE,major_courses):
    return f"You selected: {prefered_professor}, {prefered_time_range}, {GE},{major_courses}"



with gr.Blocks() as demo2:
    gr.Markdown("Hello, please enter your preferred professor and time range for initialization.")
    with gr.Row():
        with gr.Column():
            professor_dropdown = gr.Dropdown(["Prof A", "Prof B", "Prof C", "Prof D"],label="Select Professor")
               #the time range can be more specific
            time_range_dropdown = gr.Dropdown(["Around 8AM", "Around 10AM", "Around 12PM"],label="Select Time Range")
            ge = gr.Dropdown(['A','B','C','D','E','F','None'],label="Select GE Area")
            major_course=gr.Radio(['Yes','No'],label='Do you want to take your major courses')
            
            
            
            submit_button = gr.Button("Submit")
            output_text = gr.Textbox()

    submit_button.click(
        fn=dropdown_selection,
        inputs=[professor_dropdown, time_range_dropdown, ge,major_course],
        outputs=output_text
    )

demo2.launch()
