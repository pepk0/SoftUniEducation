class Email:
    def __init__(self, sender: str, receiver: str,
                 content: str, is_sent=False) -> None:
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self) -> None:
        self.is_sent = True

    def get_info(self) -> str:
        return (f"{self.sender} says to {self.receiver}: "
                f"{self.content}. Sent: {self.is_sent}")


emails = []
while 1:
    command = input()
    if command == "Stop":
        break
    sender, receiver, content = command.split()
    emails.append(Email(sender, receiver, content))

indexes = [int(i) for i in input().split(", ")]
for index in range(len(emails)):
    email = emails[index]
    if index in indexes:
        email.send()
    print(email.get_info())
