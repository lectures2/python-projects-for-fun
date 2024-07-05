import os
import PyPDF2

def remove_pdf_password(input_path, output_path):
    with open(input_path, 'rb') as input_file:
        pdf = PyPDF2.PdfReader(input_file)
        
        if not pdf.isEncrypted:
            print("The PDF is not encrypted. No password needed.")
            return
        
        # Create a list of passwords to try (you can customize this list)
        passwords_to_try = ["password", "123456", "qwerty", "test", "password123"]
        
        for password in passwords_to_try:
            if pdf.decrypt(password):
                print(f"Decryption successful with password: {password}")
                
                # Create a new PDF writer to remove the encryption
                pdf_writer = PyPDF2.PdfWriter()
                
                # Add all pages from the original PDF to the new PDF writer
                for page_num in range(len(pdf.pages)):
                    pdf_writer.add_page(pdf.pages[page_num])
                
                # Write the new PDF without encryption
                output_file = os.path.join(os.path.dirname(input_path), "decrypted.pdf")
                with open(output_file, 'wb') as output_file:
                    pdf_writer.write(output_file)
                
                return
        
        print("Decryption failed. Password not found.")

if __name__ == "__main__":
    input_file_path = r"D:\languageAcademy\Special_passing_test_question.pdf"
    
    remove_pdf_password(input_file_path, None)
