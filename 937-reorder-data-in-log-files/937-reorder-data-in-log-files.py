class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def separate_identifier(log):
            return log.split(" ")
        
        digit_logs = []
        letter_logs = []
        output = []

        for log in logs:
            if separate_identifier(log)[1].isdigit(): # digit log
                digit_logs.append(log)
            else: #
                split_log = separate_identifier(log)
                letter_logs.append((' '.join(split_log[1:]),split_log[0]))

        letter_logs.sort()
        for content,identifier in letter_logs:
            output.append(identifier + ' ' + content)
        for digit_log in digit_logs:
            output.append(digit_log)

        return output
        