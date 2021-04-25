from plyer import notification

title ="Covid-19"
message ="Covid-19 spread report"
# title,message,app_name,app_icon,timeout,ticker,toast
notification.notify(title=title, message=message,app_name="stunna",timeout=10,toast=False)