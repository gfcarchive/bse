WebBanking {
  version = 1.0,
  url = "https://google.com",
  services = {"Service Name"},
  description = "this is a description",
}

test_localizetext = string.format(MM.localizeText("This is a %s"), "Test")
test_localizenumber1 = MM.localizeNumber(1)
test_localizenumber2 = MM.localizeNumber(1.1)
test_localizenumber3 = MM.localizeNumber("#,##0.##;-#", 1.2345)
test_localizedate1 = MM.localizeDate(1585668268)
test_localizedate2 = MM.localizeDate("yyyy.MM.dd G 'at' HH:mm:ss zzz", 1585668268)
