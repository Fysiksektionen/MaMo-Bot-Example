# Mattermost Bot Example

This is a minimal configuration of a Mattermost bot to run on the Fysiksektionen mattermost server.

It consists of a mattermost driver to send requests, as well as a websocket to listen to events happening.

To find the format of a request, you can use the [Mattermost API reference](https://api.mattermost.com/#tag/posts) to do any action allowed by it. The reference describes three attributes:
- HTTP Request Method: Either POST, GET, PUT, or DELETE. Represents the kind of request to make, which is decided by the use of method on the driver.
- URL: The url to send the request to. The mattermostdriver includes the basepath, and only the endpoint and furhter arguments are required. This could also include parameters, for example emoji/name/{emoji_name} where {emoji_name} is a variable.
- Data: The data to be sent using the data parameter of the request methods.

You can also find the types of requests, but it is mostly poorly documented, and it may be better to simply print the event when given, and analys from there.

Some methods are also given by the [mattermostdriver library](https://pypi.org/project/mattermostdriver/), so you can look in the docs.

Most of the bots in the Fysiksektionen mattermost are freely available [here](https://github.com/LogFlames/mattermost-bots) and may provide good examples, a lot of reusable code, and help.
