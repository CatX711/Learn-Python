# (this is a personal file so it wont be like a tutorial. For personal files that I myself can look at and read without the in depth writing my other tutorial files, there will
# be a disclaimer, like this one)

# An email client using classes

while True:
    answer1 = input("Enter an email: ")

    class EmailClient():
        def Recieve(self):
            emails = {"email": answer1}
            print("Your email has been put into storage.")

        def Delete(self):
            emails = {"email": ""}
            print("Your email has been deleted.")


    answer = input("What do you want to do with your email? (store/del) ")
    if answer.lower() == "store":
        email_store = EmailClient()
        email_store.Recieve()
    if answer.lower() == "del":
        email_delete = EmailClient()
        email_delete.Delete()
