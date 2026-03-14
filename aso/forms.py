from django import forms

from .models import App


class AppForm(forms.ModelForm):
    """Form for creating/editing an App."""

    class Meta:
        model = App
        fields = ["name", "bundle_id"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "w-full bg-slate-700 border border-white/10 rounded-lg px-3 py-2 text-sm text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-purple-500",
                    "placeholder": "My iOS App",
                }
            ),
            "bundle_id": forms.TextInput(
                attrs={
                    "class": "w-full bg-slate-700 border border-white/10 rounded-lg px-3 py-2 text-sm text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-purple-500",
                    "placeholder": "com.example.myapp (optional)",
                }
            ),
        }


# All 184 iTunes App Store country codes (ISO 3166-1 alpha-2).
# Source: https://github.com/jcoester/iTunes-country-codes
# (auto-verified daily via GitHub Actions against iTunes Search API)
COUNTRY_CHOICES = [
    ("af", "\U0001f1e6\U0001f1eb Afghanistan"),
    ("al", "\U0001f1e6\U0001f1f1 Albania"),
    ("dz", "\U0001f1e9\U0001f1ff Algeria"),
    ("ad", "\U0001f1e6\U0001f1e9 Andorra"),
    ("ao", "\U0001f1e6\U0001f1f4 Angola"),
    ("ai", "\U0001f1e6\U0001f1ee Anguilla"),
    ("ag", "\U0001f1e6\U0001f1ec Antigua and Barbuda"),
    ("ar", "\U0001f1e6\U0001f1f7 Argentina"),
    ("am", "\U0001f1e6\U0001f1f2 Armenia"),
    ("au", "\U0001f1e6\U0001f1fa Australia"),
    ("at", "\U0001f1e6\U0001f1f9 Austria"),
    ("az", "\U0001f1e6\U0001f1ff Azerbaijan"),
    ("bs", "\U0001f1e7\U0001f1f8 Bahamas"),
    ("bh", "\U0001f1e7\U0001f1ed Bahrain"),
    ("bd", "\U0001f1e7\U0001f1e9 Bangladesh"),
    ("bb", "\U0001f1e7\U0001f1e7 Barbados"),
    ("by", "\U0001f1e7\U0001f1fe Belarus"),
    ("be", "\U0001f1e7\U0001f1ea Belgium"),
    ("bz", "\U0001f1e7\U0001f1ff Belize"),
    ("bj", "\U0001f1e7\U0001f1ef Benin"),
    ("bm", "\U0001f1e7\U0001f1f2 Bermuda"),
    ("bt", "\U0001f1e7\U0001f1f9 Bhutan"),
    ("bo", "\U0001f1e7\U0001f1f4 Bolivia"),
    ("ba", "\U0001f1e7\U0001f1e6 Bosnia and Herzegovina"),
    ("bw", "\U0001f1e7\U0001f1fc Botswana"),
    ("br", "\U0001f1e7\U0001f1f7 Brazil"),
    ("vg", "\U0001f1fb\U0001f1ec British Virgin Islands"),
    ("bn", "\U0001f1e7\U0001f1f3 Brunei"),
    ("bg", "\U0001f1e7\U0001f1ec Bulgaria"),
    ("bf", "\U0001f1e7\U0001f1eb Burkina Faso"),
    ("cv", "\U0001f1e8\U0001f1fb Cabo Verde"),
    ("kh", "\U0001f1f0\U0001f1ed Cambodia"),
    ("cm", "\U0001f1e8\U0001f1f2 Cameroon"),
    ("ca", "\U0001f1e8\U0001f1e6 Canada"),
    ("ky", "\U0001f1f0\U0001f1fe Cayman Islands"),
    ("cf", "\U0001f1e8\U0001f1eb Central African Republic"),
    ("td", "\U0001f1f9\U0001f1e9 Chad"),
    ("cl", "\U0001f1e8\U0001f1f1 Chile"),
    ("cn", "\U0001f1e8\U0001f1f3 China"),
    ("co", "\U0001f1e8\U0001f1f4 Colombia"),
    ("cg", "\U0001f1e8\U0001f1ec Congo"),
    ("cd", "\U0001f1e8\U0001f1e9 Congo (DR)"),
    ("cr", "\U0001f1e8\U0001f1f7 Costa Rica"),
    ("ci", "\U0001f1e8\U0001f1ee Cote d'Ivoire"),
    ("hr", "\U0001f1ed\U0001f1f7 Croatia"),
    ("cy", "\U0001f1e8\U0001f1fe Cyprus"),
    ("cz", "\U0001f1e8\U0001f1ff Czechia"),
    ("dk", "\U0001f1e9\U0001f1f0 Denmark"),
    ("dm", "\U0001f1e9\U0001f1f2 Dominica"),
    ("do", "\U0001f1e9\U0001f1f4 Dominican Republic"),
    ("ec", "\U0001f1ea\U0001f1e8 Ecuador"),
    ("eg", "\U0001f1ea\U0001f1ec Egypt"),
    ("sv", "\U0001f1f8\U0001f1fb El Salvador"),
    ("ee", "\U0001f1ea\U0001f1ea Estonia"),
    ("sz", "\U0001f1f8\U0001f1ff Eswatini"),
    ("et", "\U0001f1ea\U0001f1f9 Ethiopia"),
    ("fj", "\U0001f1eb\U0001f1ef Fiji"),
    ("fi", "\U0001f1eb\U0001f1ee Finland"),
    ("fr", "\U0001f1eb\U0001f1f7 France"),
    ("ga", "\U0001f1ec\U0001f1e6 Gabon"),
    ("gm", "\U0001f1ec\U0001f1f2 Gambia"),
    ("ge", "\U0001f1ec\U0001f1ea Georgia"),
    ("de", "\U0001f1e9\U0001f1ea Germany"),
    ("gh", "\U0001f1ec\U0001f1ed Ghana"),
    ("gr", "\U0001f1ec\U0001f1f7 Greece"),
    ("gd", "\U0001f1ec\U0001f1e9 Grenada"),
    ("gt", "\U0001f1ec\U0001f1f9 Guatemala"),
    ("gn", "\U0001f1ec\U0001f1f3 Guinea"),
    ("gw", "\U0001f1ec\U0001f1fc Guinea-Bissau"),
    ("gy", "\U0001f1ec\U0001f1fe Guyana"),
    ("hn", "\U0001f1ed\U0001f1f3 Honduras"),
    ("hk", "\U0001f1ed\U0001f1f0 Hong Kong"),
    ("hu", "\U0001f1ed\U0001f1fa Hungary"),
    ("is", "\U0001f1ee\U0001f1f8 Iceland"),
    ("in", "\U0001f1ee\U0001f1f3 India"),
    ("id", "\U0001f1ee\U0001f1e9 Indonesia"),
    ("iq", "\U0001f1ee\U0001f1f6 Iraq"),
    ("ie", "\U0001f1ee\U0001f1ea Ireland"),
    ("il", "\U0001f1ee\U0001f1f1 Israel"),
    ("it", "\U0001f1ee\U0001f1f9 Italy"),
    ("jm", "\U0001f1ef\U0001f1f2 Jamaica"),
    ("jp", "\U0001f1ef\U0001f1f5 Japan"),
    ("jo", "\U0001f1ef\U0001f1f4 Jordan"),
    ("kz", "\U0001f1f0\U0001f1ff Kazakhstan"),
    ("ke", "\U0001f1f0\U0001f1ea Kenya"),
    ("xk", "\U0001f1fd\U0001f1f0 Kosovo"),
    ("kw", "\U0001f1f0\U0001f1fc Kuwait"),
    ("kg", "\U0001f1f0\U0001f1ec Kyrgyzstan"),
    ("la", "\U0001f1f1\U0001f1e6 Laos"),
    ("lv", "\U0001f1f1\U0001f1fb Latvia"),
    ("lb", "\U0001f1f1\U0001f1e7 Lebanon"),
    ("lr", "\U0001f1f1\U0001f1f7 Liberia"),
    ("ly", "\U0001f1f1\U0001f1fe Libya"),
    ("li", "\U0001f1f1\U0001f1ee Liechtenstein"),
    ("lt", "\U0001f1f1\U0001f1f9 Lithuania"),
    ("lu", "\U0001f1f1\U0001f1fa Luxembourg"),
    ("mo", "\U0001f1f2\U0001f1f4 Macao"),
    ("mg", "\U0001f1f2\U0001f1ec Madagascar"),
    ("mw", "\U0001f1f2\U0001f1fc Malawi"),
    ("my", "\U0001f1f2\U0001f1fe Malaysia"),
    ("mv", "\U0001f1f2\U0001f1fb Maldives"),
    ("ml", "\U0001f1f2\U0001f1f1 Mali"),
    ("mt", "\U0001f1f2\U0001f1f9 Malta"),
    ("mr", "\U0001f1f2\U0001f1f7 Mauritania"),
    ("mu", "\U0001f1f2\U0001f1fa Mauritius"),
    ("mx", "\U0001f1f2\U0001f1fd Mexico"),
    ("fm", "\U0001f1eb\U0001f1f2 Micronesia"),
    ("md", "\U0001f1f2\U0001f1e9 Moldova"),
    ("mc", "\U0001f1f2\U0001f1e8 Monaco"),
    ("mn", "\U0001f1f2\U0001f1f3 Mongolia"),
    ("me", "\U0001f1f2\U0001f1ea Montenegro"),
    ("ms", "\U0001f1f2\U0001f1f8 Montserrat"),
    ("ma", "\U0001f1f2\U0001f1e6 Morocco"),
    ("mz", "\U0001f1f2\U0001f1ff Mozambique"),
    ("mm", "\U0001f1f2\U0001f1f2 Myanmar"),
    ("na", "\U0001f1f3\U0001f1e6 Namibia"),
    ("nr", "\U0001f1f3\U0001f1f7 Nauru"),
    ("np", "\U0001f1f3\U0001f1f5 Nepal"),
    ("nl", "\U0001f1f3\U0001f1f1 Netherlands"),
    ("nz", "\U0001f1f3\U0001f1ff New Zealand"),
    ("ni", "\U0001f1f3\U0001f1ee Nicaragua"),
    ("ne", "\U0001f1f3\U0001f1ea Niger"),
    ("ng", "\U0001f1f3\U0001f1ec Nigeria"),
    ("mk", "\U0001f1f2\U0001f1f0 North Macedonia"),
    ("no", "\U0001f1f3\U0001f1f4 Norway"),
    ("om", "\U0001f1f4\U0001f1f2 Oman"),
    ("pk", "\U0001f1f5\U0001f1f0 Pakistan"),
    ("pw", "\U0001f1f5\U0001f1fc Palau"),
    ("ps", "\U0001f1f5\U0001f1f8 Palestine"),
    ("pa", "\U0001f1f5\U0001f1e6 Panama"),
    ("pg", "\U0001f1f5\U0001f1ec Papua New Guinea"),
    ("py", "\U0001f1f5\U0001f1fe Paraguay"),
    ("pe", "\U0001f1f5\U0001f1ea Peru"),
    ("ph", "\U0001f1f5\U0001f1ed Philippines"),
    ("pl", "\U0001f1f5\U0001f1f1 Poland"),
    ("pt", "\U0001f1f5\U0001f1f9 Portugal"),
    ("qa", "\U0001f1f6\U0001f1e6 Qatar"),
    ("ro", "\U0001f1f7\U0001f1f4 Romania"),
    ("ru", "\U0001f1f7\U0001f1fa Russia"),
    ("rw", "\U0001f1f7\U0001f1fc Rwanda"),
    ("kn", "\U0001f1f0\U0001f1f3 Saint Kitts and Nevis"),
    ("lc", "\U0001f1f1\U0001f1e8 Saint Lucia"),
    ("vc", "\U0001f1fb\U0001f1e8 Saint Vincent"),
    ("ws", "\U0001f1fc\U0001f1f8 Samoa"),
    ("st", "\U0001f1f8\U0001f1f9 Sao Tome and Principe"),
    ("sa", "\U0001f1f8\U0001f1e6 Saudi Arabia"),
    ("sn", "\U0001f1f8\U0001f1f3 Senegal"),
    ("rs", "\U0001f1f7\U0001f1f8 Serbia"),
    ("sc", "\U0001f1f8\U0001f1e8 Seychelles"),
    ("sl", "\U0001f1f8\U0001f1f1 Sierra Leone"),
    ("sg", "\U0001f1f8\U0001f1ec Singapore"),
    ("sk", "\U0001f1f8\U0001f1f0 Slovakia"),
    ("si", "\U0001f1f8\U0001f1ee Slovenia"),
    ("sb", "\U0001f1f8\U0001f1e7 Solomon Islands"),
    ("za", "\U0001f1ff\U0001f1e6 South Africa"),
    ("kr", "\U0001f1f0\U0001f1f7 South Korea"),
    ("es", "\U0001f1ea\U0001f1f8 Spain"),
    ("lk", "\U0001f1f1\U0001f1f0 Sri Lanka"),
    ("sr", "\U0001f1f8\U0001f1f7 Suriname"),
    ("se", "\U0001f1f8\U0001f1ea Sweden"),
    ("ch", "\U0001f1e8\U0001f1ed Switzerland"),
    ("tw", "\U0001f1f9\U0001f1fc Taiwan"),
    ("tj", "\U0001f1f9\U0001f1ef Tajikistan"),
    ("tz", "\U0001f1f9\U0001f1ff Tanzania"),
    ("th", "\U0001f1f9\U0001f1ed Thailand"),
    ("to", "\U0001f1f9\U0001f1f4 Tonga"),
    ("tt", "\U0001f1f9\U0001f1f9 Trinidad and Tobago"),
    ("tn", "\U0001f1f9\U0001f1f3 Tunisia"),
    ("tr", "\U0001f1f9\U0001f1f7 Turkey"),
    ("tm", "\U0001f1f9\U0001f1f2 Turkmenistan"),
    ("tc", "\U0001f1f9\U0001f1e8 Turks and Caicos"),
    ("ae", "\U0001f1e6\U0001f1ea UAE"),
    ("ug", "\U0001f1fa\U0001f1ec Uganda"),
    ("ua", "\U0001f1fa\U0001f1e6 Ukraine"),
    ("gb", "\U0001f1ec\U0001f1e7 United Kingdom"),
    ("us", "\U0001f1fa\U0001f1f8 United States"),
    ("uy", "\U0001f1fa\U0001f1fe Uruguay"),
    ("uz", "\U0001f1fa\U0001f1ff Uzbekistan"),
    ("vu", "\U0001f1fb\U0001f1fa Vanuatu"),
    ("ve", "\U0001f1fb\U0001f1ea Venezuela"),
    ("vn", "\U0001f1fb\U0001f1f3 Vietnam"),
    ("ye", "\U0001f1fe\U0001f1ea Yemen"),
    ("zm", "\U0001f1ff\U0001f1f2 Zambia"),
    ("zw", "\U0001f1ff\U0001f1fc Zimbabwe"),
]


class KeywordSearchForm(forms.Form):
    """Form for searching keywords."""

    keywords = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full bg-slate-700 border border-white/10 rounded-lg px-3 py-2 text-sm text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-purple-500",
                "placeholder": "meditation app, fitness tracker, sleep sounds",
                "autofocus": True,
            }
        ),
        label="Keywords",
        help_text="Enter one or more keywords, separated by commas (max 20).",
    )
    app_id = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput(),
    )
    countries = forms.CharField(
        required=False,
        widget=forms.HiddenInput(),
        help_text="Comma-separated country codes (max 5).",
    )

    def clean_countries(self):
        """Parse and validate comma-separated country codes."""
        raw = self.cleaned_data.get("countries", "").strip()
        if not raw:
            return ["us"]
        valid_codes = {code for code, _ in COUNTRY_CHOICES}
        codes = [c.strip().lower() for c in raw.split(",") if c.strip()]
        codes = [c for c in codes if c in valid_codes]
        if not codes:
            return ["us"]
        return codes[:5]  # Max 5 countries


class OpportunitySearchForm(forms.Form):
    """Form for the Country Opportunity Finder — single keyword, all countries."""

    keyword = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "w-full bg-slate-700 border border-white/10 rounded-lg px-3 py-2 text-sm text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-purple-500",
                "placeholder": "fitness tracker",
                "autofocus": True,
            }
        ),
    )
    app_id = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput(),
    )
