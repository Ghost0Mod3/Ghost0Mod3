import json
import os


class TargetManager:

    def __init__(self):

        self.data_dir = "data"
        self.target_file = os.path.join(
            self.data_dir,
            "target.json"
        )

        os.makedirs(
            self.data_dir,
            exist_ok=True
        )

    def save_target(self, network):

        try:

            with open(
                self.target_file,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    network,
                    file,
                    indent=4
                )

            return True

        except Exception as error:

            print(
                f"Failed to save target: {error}"
            )

            return False

    def load_target(self):

        try:

            if not os.path.exists(
                self.target_file
            ):
                return None

            with open(
                self.target_file,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        except Exception as error:

            print(
                f"Failed to load target: {error}"
            )

            return None

    def clear_target(self):

        try:

            if os.path.exists(
                self.target_file
            ):

                os.remove(
                    self.target_file
                )

            return True

        except Exception as error:

            print(
                f"Failed to clear target: {error}"
            )

            return False

    def has_target(self):

        return os.path.exists(
            self.target_file
        )
