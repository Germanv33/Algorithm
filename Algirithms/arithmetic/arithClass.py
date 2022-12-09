from decimal import Decimal

class ArithmeticEncoding:

   
    def __init__(self, probability_table):
        """
        frequency_table: Таблица частот в виде словаря, где ключ - символ, а значение - частота.
        # """
    
        self.probability_table = probability_table

    def process_stage(self, probability_table, stage_min, stage_max):
        """
        Обработка этапа в процессе кодирования/декодирования.
        таблица_вероятностей: Таблица вероятностей.
        stage_min: Минимальная вероятность текущего этапа.
        stage_max: Максимальная вероятность текущего этапа.
        
        Возвращает вероятности на этапе.
        """

        stage_probs = {}
        stage_domain = stage_max - stage_min
        for term_idx in range(len(probability_table.items())):
            term = list(probability_table.keys())[term_idx]
            term_prob = Decimal(probability_table[term])
            cum_prob = term_prob * stage_domain + stage_min
            stage_probs[term] = [stage_min, cum_prob]
            stage_min = cum_prob
        return stage_probs

    

    def get_encoded_value(self, last_stage_probs):
        """
        После кодирования всего сообщения этот метод возвращает единственное значение, которое представляет все сообщение.
        last_stage_probs: Список вероятностей на последнем этапе.
        
        Возвращает минимальную и максимальную вероятности на последнем этапе в дополнение к значению, кодирующему сообщение.
        """
        last_stage_probs = list(last_stage_probs.values())
        last_stage_values = []
        for sublist in last_stage_probs:
            for element in sublist:
                last_stage_values.append(element)

        last_stage_min = min(last_stage_values)
        last_stage_max = max(last_stage_values)
        encoded_value = (last_stage_min + last_stage_max)/2

        return last_stage_min, last_stage_max, encoded_value

    def encode(self, msg, probability_table):
        """
        Кодирует сообщение с помощью арифметического кодирования.
        msg: Сообщение, которое нужно закодировать.
        probability_table: Таблица вероятностей.
        Возвращает кодировщик, значение с плавающей точкой, представляющее закодированное сообщение, а также максимальное и минимальное значения интервала, в который попадает значение с плавающей точкой.
        """
        
        msg = list(msg)

        stage_min = Decimal(0.0)
        stage_max = Decimal(1.0)

        for msg_term_idx in range(len(msg)):
            stage_probs = self.process_stage(probability_table, stage_min, stage_max)

            msg_term = msg[msg_term_idx]
            stage_min = stage_probs[msg_term][0]
            stage_max = stage_probs[msg_term][1]



        last_stage_probs = self.process_stage(probability_table, stage_min, stage_max)


        interval_min_value, interval_max_value, encoded_msg = self.get_encoded_value(last_stage_probs)

        return encoded_msg, interval_min_value, interval_max_value 

    
