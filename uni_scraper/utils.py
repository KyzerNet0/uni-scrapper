import re
import tldextract

EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

# filter bad emails
def clean_emails(emails, domain):
    cleaned = []

    for email in emails:
        email = email.lower()

        # skip junk
        if any(x in email for x in ["example", "test", "fake", "noreply"]):
            continue

        # prefer same domain
        if domain in email:
            cleaned.append(email)

    return list(set(cleaned))


def extract_domain(url):
    ext = tldextract.extract(url)
    return ext.domain


def find_emails(text):
    return re.findall(EMAIL_REGEX, text)
