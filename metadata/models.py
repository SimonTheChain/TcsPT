from django.db import models
from django.core.urlresolvers import reverse
from datetime import date
from operator import itemgetter

from projectmanage.models import Project


ITUNES_GENRES = (
        ("", ""),
        ("ACTION-ADVENTURE-00", "Action & Adventure"),
        ("AFRICAN-00", "African"),
        ("ANIME-00", "Anime"),
        ("BOLLYWOOD-00", "Bollywood"),
        ("CLASSICS-00", "Classics"),
        ("COMEDY-00", "Comedy"),
        ("CONCERT-FILMS-00", "Concert Films"),
        ("DOCUMENTARY-00", "Documentary"),
        ("DRAMA-00", "Drama"),
        ("FOREIGN-00", "Foreign"),
        ("HOLIDAY-00", "Holiday"),
        ("HORROR-00", "Horror"),
        ("INDEPENDENT-00", "Independent"),
        ("KIDS-FAMILY-00", "Kids & Family"),
        ("MADE-FOR-TV-00", "Made for TV"),
        ("MIDDLE-EASTERN-00", "Middle Eastern"),
        ("MUSIC-DOCUMENTARIES-00", "Music Documentaries"),
        ("MUSIC-FEATURE-FILMS-00", "Music Feature Film"),
        ("MUSICALS-00", "Musicals"),
        ("REGIONAL-INDIAN-00", "Regional Indian"),
        ("ROMANCE-00", "Romance"),
        ("RUSSIAN-00", "Russian"),
        ("SCIFI-FANTASY-00", "Sci-Fi & Fantasy"),
        ("SHORT-FILMS-00", "Short Films"),
        ("SPECIAL-INTEREST-00", "Special Interest"),
        ("SPORTS-00", "Sports"),
        ("THRILLER-00", "Thriller"),
        ("TURKISH-00", "Turkish"),
        ("URBAN-00", "Urban"),
        ("WESTERN-00", "Western"),
    )


ITUNES_RATINGS = (
        ("", ""),
        ("ai-movies", "AI"),
        ("ag-movies", "AG"),
        ("ar-movies", "AR"),
        ("am-movies", "AM"),
        ("au-oflc", "AU"),
        ("fsk", "AT"),
        ("az-movies", "AZ"),
        ("bs-movies", "BS"),
        ("bh-movies", "BH"),
        ("bb-movies", "BB"),
        ("by-movies", "BY"),
        ("be-movies", "BE"),
        ("bz-movies", "BZ"),
        ("bm-movies", "BM"),
        ("bo-movies", "BO"),
        ("bw-movies", "BW"),
        ("br-movies", "BR"),
        ("vg-movies", "VG"),
        ("bn-movies", "BN"),
        ("bg-movies", "BG"),
        ("bf-movies", "BF"),
        ("kh-movies", "KH"),
        ("ca-chvrs", "CA"),
        ("cv-movies", "CV"),
        ("ky-movies", "KY"),
        ("cl-movies", "CL"),
        ("cn-movies", "CN"),
        ("co-movies", "CO"),
        ("cr-movies", "CR"),
        ("cy-movies", "CY"),
        ("cz-movies", "CZ"),
        ("dk-movies", "DK"),
        ("dm-movies", "DM"),
        ("do-movies", "DO"),
        ("ec-movies", "EC"),
        ("eg-movies", "EG"),
        ("sv-movies", "SV"),
        ("ee-movies", "EE"),
        ("fm-movies", "FM"),
        ("fj-movies", "FJ"),
        ("fi-movies", "FI"),
        ("fr-cnc", "FR"),
        ("gm-movies", "GM"),
        ("de-fsk", "DE"),
        ("gh-movies", "GH"),
        ("gr-movies", "GR"),
        ("gd-movies", "GD"),
        ("gt-movies", "GT"),
        ("gw-movies", "GW"),
        ("gy-movies", "GY"),
        ("hn-movies", "HN"),
        ("hk-movies", "HK"),
        ("hu-movies", "HU"),
        ("in-movies", "IN"),
        ("id-movies", "ID"),
        ("ie-ifco", "IE"),
        ("il-movies", "IL"),
        ("it-movies", "IT"),
        ("jm-movies", "JM"),
        ("jp-eirin", "JP"),
        ("jo-movies", "JO"),
        ("kz-movies", "KZ"),
        ("ke-movies", "KE"),
        ("kr-movies", "KR"),
        ("kg-movies", "KG"),
        ("la-movies", "LA"),
        ("lv-movies", "LV"),
        ("lb-movies", "LB"),
        ("lt-movies", "LT"),
        ("lu-movies", "LU"),
        ("mo-movies", "MO"),
        ("my-movies", "MY"),
        ("mt-movies", "MT"),
        ("mu-movies", "MU"),
        ("mx-movies", "MX"),
        ("md-movies", "MD"),
        ("mn-movies", "MN"),
        ("mz-movies", "MZ"),
        ("na-movies", "NA"),
        ("np-movies", "NP"),
        ("nl-movies", "NL"),
        ("nz-oflc", "NZ"),
        ("ni-movies", "NI"),
        ("ne-movies", "NE"),
        ("ng-movies", "NG"),
        ("no-movies", "NO"),
        ("om-movies", "OM"),
        ("pa-movies", "PA"),
        ("pg-movies", "PG"),
        ("py-movies", "PY"),
        ("pe-movies", "PE"),
        ("ph-movies", "PH"),
        ("pl-movies", "PL"),
        ("pt-movies", "PT"),
        ("qa-movies", "QA"),
        ("ca-rcq", "QC"),
        ("ro-movies", "RO"),
        ("ru-movies", "RU"),
        ("kn-movies", "KN"),
        ("sa-movies", "SA"),
        ("sg-movies", "SG"),
        ("sk-movies", "SK"),
        ("si-movies", "SI"),
        ("za-movies", "ZA"),
        ("es-movies", "ES"),
        ("lk-movies", "LK"),
        ("sz-movies", "SZ"),
        ("se-movies", "SE"),
        ("ch-movies", "CH"),
        ("tw-movies", "TW"),
        ("tj-movies", "TJ"),
        ("th-movies", "TH"),
        ("tt-movies", "TT"),
        ("tr-movies", "TR"),
        ("tm-movies", "TM"),
        ("ug-movies", "UG"),
        ("ua-movies", "UA"),
        ("ae-movies", "AE"),
        ("bbfc", "GB"),
        ("mpaa", "US"),
        ("uy-movies", "UY"),
        ("uz-movies", "UZ"),
        ("ve-movies", "VE"),
        ("vn-movies", "VN"),
        ("zw-movies", "ZW"),
    )
ratings_sorted = sorted(ITUNES_RATINGS, key=itemgetter(1))


CREW_ROLES = (
    ("", ""),
    ("Director", "Director"),
    ("Producer", "Producer"),
    ("Screenwriter", "Screenwriter"),
    ("Composer", "Composer"),
    ("Co-Director", "Co-Director"),
)


SASKTEL_AUDIO_TYPES = (
    ("Dolby 5.1", "Dolby 5.1"),
    ("Stereo", "Stereo"),
)


SASKTEL_SCREEN_FORMATS = (
    ("Standard", "Standard"),
    ("Widescreen", "Widescreen"),
    ("Letterbox", "Letterbox"),
    ("OAR", "OAR"),
)


class Metadata(models.Model):

    # generic info
    studio_release_title = models.CharField(max_length=250, default="")
    original_language = models.CharField(max_length=10, default="", blank=True)
    country_of_origin = models.CharField(max_length=2, default="", blank=True)
    copyright_line = models.CharField(max_length=250, default="", blank=True)
    release_date = models.DateField(default=date.today, blank=True, null=True)
    production_company = models.CharField(max_length=250, default="", blank=True)
    cast = models.CharField(max_length=1000, default="", blank=True)
    crew = models.CharField(max_length=1000, default="", blank=True)
    genres = models.CharField(max_length=250, default="", blank=True)
    chvrs_rating = models.CharField(max_length=250, default="", blank=True)
    rcq_rating = models.CharField(max_length=250, default="", blank=True)

    # localization
    title_en = models.CharField(max_length=250, default="", blank=True)
    synopsis_long_en = models.CharField(max_length=1000, default="", blank=True)
    synopsis_short_en = models.CharField(max_length=250, default="", blank=True)
    title_fr = models.CharField(max_length=250, default="", blank=True)
    synopsis_long_fr = models.CharField(max_length=1000, default="", blank=True)
    synopsis_short_fr = models.CharField(max_length=250, default="", blank=True)

    # itunes info
    itunes_vendor_id = models.CharField(max_length=250, default="", blank=True)
    itunes_territories = models.CharField(max_length=250, default="", blank=True)
    itunes_cleared_sale = models.BooleanField(default=True)
    itunes_cleared_preorder = models.BooleanField(default=True)
    itunes_preoder_date = models.DateField(default=date.today, blank=True, null=True)
    itunes_est_start_date = models.DateField(default=date.today, blank=True, null=True)
    itunes_est_end_date = models.DateField(default=date.today, blank=True, null=True)
    itunes_cleared_vod = models.BooleanField(default=True)
    itunes_vod_start_date = models.DateField(default=date.today, blank=True, null=True)
    itunes_vod_end_date = models.DateField(default=date.today, blank=True, null=True)
    itunes_home_video_date = models.DateField(default=date.today, blank=True, null=True)
    itunes_sd_price_tier = models.IntegerField(default=0, blank=True)
    itunes_hd_price_tier = models.IntegerField(default=0, blank=True)
    itunes_library = models.BooleanField(default=False)

    # google info
    google_channel = models.CharField(max_length=250, default="", blank=True)
    google_custom_id = models.CharField(max_length=250, default="", blank=True)
    google_genre_1 = models.CharField(max_length=250, default="", blank=True)
    google_genre_2 = models.CharField(max_length=250, default="", blank=True)
    google_genre_3 = models.CharField(max_length=250, default="", blank=True)
    google_genre_4 = models.CharField(max_length=250, default="", blank=True)
    google_rating_system_1 = models.CharField(max_length=250, default="", blank=True)
    google_rating_system_2 = models.CharField(max_length=250, default="", blank=True)
    google_rating_system_3 = models.CharField(max_length=250, default="", blank=True)
    google_rating_system_4 = models.CharField(max_length=250, default="", blank=True)
    google_video_order_id = models.CharField(max_length=250, default="", blank=True)
    google_territories = models.CharField(max_length=250, default="", blank=True)

    # sasktel info
    sasktel_billing_id = models.CharField(max_length=250, default="", blank=True)
    sasktel_inventory_id = models.CharField(max_length=250, default="", blank=True)
    sasktel_lineup_id = models.CharField(max_length=250, default="", blank=True)
    sasktel_category_1 = models.CharField(max_length=250, default="", blank=True)
    sasktel_category_2 = models.CharField(max_length=250, default="", blank=True)
    sasktel_category_3 = models.CharField(max_length=250, default="", blank=True)
    sasktel_category_4 = models.CharField(max_length=250, default="", blank=True)
    sasktel_closed_captioning = models.BooleanField(default=True)
    sasktel_license_start_date = models.DateField(default=date.today, blank=True, null=True)
    sasktel_license_end_date = models.DateField(default=date.today, blank=True, null=True)
    sasktel_rating = models.CharField(max_length=10, default="NR", blank=True)
    sasktel_run_time = models.CharField(max_length=250, default="", blank=True)
    sasktel_sd_price = models.FloatField(default=5.95)
    sasktel_hd_price = models.FloatField(default=6.95)
    sasktel_title_long = models.CharField(max_length=40, default="", blank=True)
    sasktel_title_brief = models.CharField(max_length=19, default="", blank=True)
    sasktel_year = models.IntegerField(default=2016, blank=True)
    sasktel_dvd_release = models.DateField(default=date.today, blank=True, null=True)
    sasktel_canadian_content = models.BooleanField(default=False)
    sasktel_copyright = models.CharField(max_length=250, default="", blank=True)
    sasktel_feature_audio_type = models.CharField(
        max_length=250, choices=SASKTEL_AUDIO_TYPES, default="Dolby 5.1", blank=True)
    sasktel_feature_screen_format = models.CharField(
        max_length=250, choices=SASKTEL_SCREEN_FORMATS, default="Widescreen", blank=True)
    sasktel_feature_hd_content = models.BooleanField(default=True)
    sasktel_feature_subtitle_language = models.CharField(max_length=2, default="", blank=True)
    sasktel_trailer_audio_type = models.CharField(
        max_length=250, choices=SASKTEL_AUDIO_TYPES, default="Stereo", blank=True)
    sasktel_trailer_screen_format = models.CharField(
        max_length=250, choices=SASKTEL_SCREEN_FORMATS, default="Widescreen", blank=True)
    sasktel_trailer_hd_content = models.BooleanField(default=True)
    sasktel_trailer_subtitle_language = models.CharField(max_length=2, default="", blank=True)

    # foreign key
    project = models.OneToOneField(Project, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("metadata:metadata_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.studio_release_title
