"""
SlickDesk - Email Notification Automation
Sends auto-reply emails when a ticket is submitted.
Uses Gmail SMTP (or replace with SendGrid API).
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# CONFIG — replace with your actual credentials or use environment variables
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv("SLICKDESK_EMAIL", "your@gmail.com")
SENDER_PASSWORD = os.getenv("SLICKDESK_PASSWORD", "your_app_password")

def send_confirmation_email(recipient_email, recipient_name, ticket_id, category, priority):
    """
    Sends a confirmation email to the user after ticket submission.
    """
    subject = f"[SlickDesk] Ticket #{ticket_id} Received - {category}"

    body = f"""
Hi {recipient_name},

Thank you for contacting the IT Helpdesk!

Your ticket has been received and is being reviewed by our team.

Ticket Details:
---------------------------------
Ticket ID  : #{ticket_id}
Category   : {category}
Priority   : {priority}
Status     : Open
---------------------------------

We will get back to you as soon as possible.
For urgent concerns, please reply to this email.

Best regards,
SlickDesk IT Support
slicklab.digital
    """

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        print(f"Confirmation email sent to {recipient_email}")
        return True
    except Exception as e:
        print(f"Email failed: {e}")
        return False


if __name__ == "__main__":
    # Test the function
    send_confirmation_email(
        recipient_email="test@example.com",
        recipient_name="Test User",
        ticket_id=1,
        category="Hardware",
        priority="High"
    )
