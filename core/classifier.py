# core/classifier.py


class Classifier:

    FLOCK_KEYWORDS = [
        "flock",
        "falcon",
        "lpr",
        "plate",
        "flocksafety",
    ]

    CAMERA_KEYWORDS = [
        "camera",
        "cam",
        "cctv",
        "hikvision",
        "dahua",
        "axis",
        "ring",
        "arlo",
        "nest",
        "reolink",
        "amcrest",
    ]

    POLICE_KEYWORDS = [
        "police",
        "sheriff",
        "trooper",
        "marshal",
        "law enforcement",
        "public safety",
        "state patrol",
    ]

    HOME_KEYWORDS = [
        "home",
        "house",
        "mywifi",
        "family",
        "linksys",
        "netgear",
        "xfinity",
        "spectrum",
        "att",
        "verizon",
        "tp-link",
    ]

    @staticmethod
    def has_keyword(text, keywords):

        text = text.lower()

        return any(
            keyword in text
            for keyword in keywords
        )

    @staticmethod
    def score_risk(ssid, crypto):

        ssid = ssid.lower()

        crypto = crypto.upper()

        if (
            "OPEN" in crypto
            or "UNKNOWN" in crypto
            or "WEP" in crypto
        ):
            return "HIGH"

        if any(
            word in ssid
            for word in [
                "free",
                "public",
                "guest",
                "airport",
                "hotel",
            ]
        ):
            return "HIGH"

        if any(
            word in ssid
            for word in [
                "wifi",
                "cafe",
                "internet",
            ]
        ):
            return "MEDIUM"

        return "LOW"

    @staticmethod
    def classify(ssid, crypto):

        ssid_lower = ssid.lower()

        if Classifier.has_keyword(
            ssid_lower,
            Classifier.FLOCK_KEYWORDS
        ):
            return {
                "category": "FLOCK",
                "risk": "HIGH"
            }

        if Classifier.has_keyword(
            ssid_lower,
            Classifier.POLICE_KEYWORDS
        ):
            return {
                "category": "POLICE",
                "risk": "HIGH"
            }

        if Classifier.has_keyword(
            ssid_lower,
            Classifier.CAMERA_KEYWORDS
        ):
            return {
                "category": "CAMERA",
                "risk": "HIGH"
            }

        if Classifier.has_keyword(
            ssid_lower,
            Classifier.HOME_KEYWORDS
        ):
            return {
                "category": "HOME",
                "risk": "LOW"
            }

        return {
            "category": "GENERAL",
            "risk": Classifier.score_risk(
                ssid,
                crypto
            )
        }