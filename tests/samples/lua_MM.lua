WebBanking {
  version = 1.0,
  url = "https://google.com",
  services = {"Service Name"},
  description = "this is a description",
}

--
test_product_name = MM.productName
test_product_version = MM.productVersion
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
test_urldecode1 = MM.urldecode("this%20is%20a%20test")
--
test_encoded_str1 = MM.toEncoding("UTF-8", "test")
test_decoded_str1 = MM.fromEncoding("UTF-8", test_encoded_str1)
test_base64_encode1 = MM.base64(test_encoded_str1)
test_base64_decode1 = MM.base64decode(test_base64_encode1)
--
test_sha512 = MM.sha512("text to hash")
test_sha256 = MM.sha256("text to hash")
test_sha1 = MM.sha1("text to hash")
test_md5 = MM.md5("text to hash")
--
test_hmac512 = MM.hmac512("secret-shared-key-goes-here", "this is the data to encrypt")
test_hmac384 = MM.hmac384("secret-shared-key-goes-here", "this is the data to encrypt")
test_hmac256 = MM.hmac256("secret-shared-key-goes-here", "this is the data to encrypt")
--
test_time = MM.time()
--
MM.sleep(1)
--
MM.printStatus(test_time)
