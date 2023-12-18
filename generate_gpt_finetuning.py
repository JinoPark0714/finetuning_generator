from GPTFineTuningGenerator import GPTFineTuningGenerator

def generate_gpt_finetuning_data():
    gpt_finetuning_generator = GPTFineTuningGenerator()
    is_system_constant = "n"
    while True:
        if(is_system_constant == "n" or is_system_constant == "N"):
                system_content = input("system 메시지 : ")
                is_system_constant = input("system 메시지 일관성 유무 (y / n or Y / N): ")
        
        user_content = input("user(끝내고 싶으면 '종료' 입력): ")
        if(user_content == "종료"):
            break

        assistant_content = input("assistant: ")
        

        gpt_finetuning_generator.write_json(
            system_content=system_content, 
            user_content=user_content, 
            assistant_content=assistant_content)