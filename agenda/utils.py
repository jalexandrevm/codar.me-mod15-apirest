from datetime import datetime, timedelta, timezone


def data_str_to_datetime_list(data_str):
    dt_obj = datetime.fromisoformat(data_str).replace(tzinfo=timezone.utc)
    lista_horas = []
    hora1 = datetime(dt_obj.year, dt_obj.month, dt_obj.day, hour=9, tzinfo=timezone.utc)
    hora_almoco_ini = datetime(
        dt_obj.year, dt_obj.month, dt_obj.day, hour=12, tzinfo=timezone.utc
    )
    hora_almoco_fim = datetime(
        dt_obj.year, dt_obj.month, dt_obj.day, hour=13, tzinfo=timezone.utc
    )
    hora_fim_dia = datetime(
        dt_obj.year, dt_obj.month, dt_obj.day, hour=18, tzinfo=timezone.utc
    )
    if dt_obj.weekday() <= 4:
        while hora1 < hora_fim_dia:
            if not (hora_almoco_ini <= hora1 < hora_almoco_fim):
                lista_horas.append(hora1)
            hora1 += timedelta(minutes=30)
        return lista_horas
    elif dt_obj.weekday() == 5:
        while hora1 < hora_almoco_fim:
            lista_horas.append(hora1)
            hora1 += timedelta(minutes=30)
        return lista_horas
