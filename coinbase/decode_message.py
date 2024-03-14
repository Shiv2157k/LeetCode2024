class SecretMessage:
    def decode_v1(self, key: str, message: str) -> str:
        """
        Python string in built methods
        :param key:
        :param message:
        :return:
        """
        index = 0
        key_table = {}
        lower_alphabets = [chr(ord('a') + i) for i in range(26)]

        for char in key:
            if char.isalpha() and char not in key_table:
                key_table[char] = lower_alphabets[index]
                index += 1
        translation_table = str.maketrans(key_table)
        return message.translate(translation_table)

    def decode_v0(self, key: str, message: str) -> str:
        """
        Approach: HashMap and list
        T: O(N)
        S: O(N)
        :param key:
        :param message:
        :return:
        """
        index = 0
        key_table = {}
        lower_alphabets = [chr(ord('a') + i) for i in range(26)]

        for char in key:
            if char.isalpha() and char not in key_table:
                key_table[char] = lower_alphabets[index]
                index += 1

        decoded_message = []
        for char in message:
            if char.isalpha():
                decoded_message.append(key_table[char])
            else:
                decoded_message.append(char)
        return ''.join(decoded_message)


if __name__ == "__main__":
    secret_message = SecretMessage()
    print(secret_message.decode_v0(
        "the quick brown fox jumps over the lazy dog",
        "vkbs bs t suepuv"
    ))
    print(secret_message.decode_v1(
        "the quick brown fox jumps over the lazy dog",
        "vkbs bs t suepuv"
    ))
