import webapp2
import caesar
import cgi

def build_page(textarea_content):
    rot_label = "<label>Rotate By </label>"
    rotation_input = "<input type='number' name='rotation'/>"
    messsage_label = "<label>Text to Encrypt </label>"
    textarea = "<textarea name='message'>" + textarea_content + "</textarea>"
    submit = "<input type='submit'/>"
    header = "<h2>Web Caesar</h2>"

    form = ("<form method='post'>" +  rot_label + rotation_input
    + "<br>"+ messsage_label + textarea + "<br>" + submit + "</form>")

    return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        rotation = int(self.request.get("rotation"))
        encrypted_message = caesar.encrypt(message, rotation)
        escaped_msg = cgi.escape(encrypted_message)
        content = build_page(escaped_msg)
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
