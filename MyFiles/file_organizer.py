import os

def create_directories():
    main_directory = "MyFiles"
    subdirectories = ["Docs", "Images", "Videos"]

    try:
        os.mkdir(main_directory)
        print(f"Directory '{main_directory}' created successfully.")
        
        for subdir in subdirectories:
            os.mkdir(os.path.join(main_directory, subdir))
            print(f"Subdirectory '{subdir}' created successfully inside '{main_directory}'.")

    except FileExistsError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    create_directories()
