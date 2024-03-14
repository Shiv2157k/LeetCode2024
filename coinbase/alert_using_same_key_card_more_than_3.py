import heapq as hq
from typing import List


class KeyCard:

    def alert_names(self, key_name: List[str], key_time: List[str]) -> List[str]:
        """
        Approach: Heapq and HashMap
        T: O(N log N)
        S: O(N)
        :param key_name:
        :param key_time:
        :return:
        """
        def get_timestamp(time: str) -> int:
            hour, minutes = list(map(int, time.split(":")))
            return (hour * 60) + minutes

        def is_with_in_an_hour(t1: int, t3: int) -> bool:
            if t3 - t1 <= 60:
                return True
            return False

        records = {}
        alerts = set()
        combined_record_sort = sorted(zip(key_name, key_time), key=lambda x: x[1])

        for name, time in combined_record_sort:
            if name not in alerts:
                records[name] = records.get(name, [])
                timestamp = get_timestamp(time)
                hq.heappush(records[name], timestamp)

                if len(records[name]) == 3:
                    t1 = hq.heappop(records[name])
                    t2 = hq.heappop(records[name])
                    t3 = hq.heappop(records[name])
                    if is_with_in_an_hour(t1, t3):
                        alerts.add(name)
                    else:
                        hq.heappush(records[name], t2)
                        hq.heappush(records[name], t3)
        return sorted(list(alerts))

    def alert_names_v0(self, key_name: List[str], key_time: List[str]) -> List[str]:
        """
        Approach: HashMap, Intelligent Find
        T: O(N log N)
        S: O(N)
        :param key_name:
        :param key_time:
        :return:
        """
        records = {}
        alerts = []

        for name, time in zip(key_name, key_time):
            records[name] = records.get(name, [])
            records[name].append(int(time.replace(':', '')))

        for name, time_list in records.items():
            time_list.sort()
            for index in range(2, len(time_list)):
                t3 = time_list[index]
                t1 = time_list[index - 2]
                if t3 - t1 <= 100:
                    alerts.append(name)
                    break
        return sorted(alerts)


if __name__ == "__main__":

    key_card = KeyCard()
    print(key_card.alert_names(
        ["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"],
        ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]
    ))
    print(key_card.alert_names_v0(
        ["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"],
        ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]
    ))


