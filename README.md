# VkMessage
Описание программы на русском:
Привет Мир, хочу поделиться своим проектом, возможно кому-нибудь эта задумка покажется интересной или полезной.
Это приложение, главной задачей которого является шифрование файлов с целью сокрытия их содержимого.
Шифрование происходит за счет испольщования модуля pyAesCrypt, который использует стандарт шифрования AES256-CBC.
В защифрованном виде файлы можно хранить на компьюторе или передать другому человеку любым способом.
Для удобства был создан пользовательский интерфейс (UI) на базе модуля Tkinter.
Для выполнения непосредственного шифрования нужно создать папку, нажав специальную кнопку в приложении. Папка автоматически появится на рабочем столе.
Далее в нее нужно перенести файлы, требующие защиты, ввести пароль в поле для пароля и нажать на галочку.
После этого автоматически произойдет шифрование.
Для расшифровки нужно перейти в раздел "Расшифровать", ввести пароль и нажать галлочку.
После этого в папке окажутся файлы в первоначальном виде.

Description of the program in Russian:
Hello World, I want to share my project, maybe someone will find this idea interesting or useful.
This is an application whose main task is to encrypt files in order to hide their contents.
Encryption is done using the pyAesCrypt module, which uses the AES256-CBC encryption standard.
Encrypted files can be stored on a computer or transferred to another person in any way.
For convenience, a user interface (UI) was created based on the Tkinter module.
To perform direct encryption, you need to create a folder by pressing a special button in the application. The folder will automatically appear on your desktop.
Next, you need to transfer files that require protection to it, enter the password in the password field and click on the checkmark.
After that, encryption will automatically occur.
To decrypt, go to the "Decrypt" section, enter the password and click the checkmark.
After that, the files will be in the folder in their original form.
