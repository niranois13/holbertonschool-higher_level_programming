import os

def generate_invitations(template_content, attendees):
    """
    Function used to generate personalized initation files from a template
    with placeholders and a list of objects.
    Each output file should be named sequentially, starting from 1.
    :param template_content: str, the template used to create the invitations
    :param attendees: list of dictionnaries, the personnalized information
                      to fill the template with.
    Returns - The function exits with a message on ERRORS.
    """
    try:
        with open("template.txt", "r") as template_file:
            template_content = template_file.read()
    except FileNotFoundError:
        print("Template file not found.")
        return

    if not template_content:
        print("Template is empty, no output files generated.")
        return("Template is empty, no output files generated.")
    if not attendees:
        print("No data provided, no output files generated.")
        return("No data provided, no output files generated.")

    if not isinstance(template_content, str):
        print("Template is not a string.")
        return
    if not isinstance(attendees, list) or not \
        all(isinstance(attendee, dict) for attendee in attendees):
        print("Attendees is not a list of dictionaries.")
        return

    for iterate, attendee in enumerate(attendees, start=1):
        try:
            output = template_content.format(
                name=attendee.get("name" or "N/A"),
                event_title=attendee.get("event_title" or "N/A"),
                event_date=attendee.get("event_date" or "N/A"),
                event_location=attendee.get("event_location" or "N/A")
            )

            with open(f"output_{iterate}.txt", "w") as f:
                f.write(output)

        except KeyError as e:
            return f("Missing key in attendee date: {e}")

    return "Invitation successfully generated."
