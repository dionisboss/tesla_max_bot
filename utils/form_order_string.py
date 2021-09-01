async def form_order_string(data_:dict):
    string_ = f"Вы  выбрали: \n" \
              f"Пол: {data_.get('gender')}\n" \
              f"Возраст: {data_.get('age')}\n" \
              f"Телосложение: {data_.get('body')}\n" \
              f"Бюджет: {data_.get('budget')}\n" \
              f"Время встречи: {data_.get('date_time')}\n" \
              f"Адрес встречи: {data_.get('address')}\n" \
              f"Пожелания: {data_.get('preferences')}\n" \
              f"Контактная информация: {data_.get('contact')}\n"
    return string_
