WebBanking {
  version = 1.0,
  url = "https://google.com",
  services = {"Service Name"},
  description = "this is a description",
}

--
test_localizetext = string.format(MM.localizeText("This is a %s"), "Test")
--
test_localizenumber1 = MM.localizeNumber(1)
test_localizenumber2 = MM.localizeNumber(1.1)
test_localizenumber3 = MM.localizeNumber("#,##0.##;-#", 1.2345)
--
test_localizedate1 = MM.localizeDate(1585668268)
test_localizedate2 = MM.localizeDate("yyyy.MM.dd G 'at' HH:mm:ss zzz", 1585668268)
--
test_localizeamount1 = MM.localizeAmount(1)
test_localizeamount2 = MM.localizeAmount(1.1)
test_localizeamount3 = MM.localizeAmount("#,##0.##;-#", 1.1)
test_localizeamount4 = MM.localizeAmount("¤#,##0.##;-#", 1.1, "EUR")
test_localizeamount5 = MM.localizeAmount(1.1, "EUR")
--
test_urlencode1 = MM.urlencode("this is a test")
test_urlencode2 = MM.urlencode("this is a test", "UTF-8")
--
