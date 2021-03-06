#!/usr/bin/env python3

# pylint:disable=line-too-long
"""
The tool to check the availability or syntax of domains, IPv4 or URL.

::


    ██████╗ ██╗   ██╗███████╗██╗   ██╗███╗   ██╗ ██████╗███████╗██████╗ ██╗     ███████╗
    ██╔══██╗╚██╗ ██╔╝██╔════╝██║   ██║████╗  ██║██╔════╝██╔════╝██╔══██╗██║     ██╔════╝
    ██████╔╝ ╚████╔╝ █████╗  ██║   ██║██╔██╗ ██║██║     █████╗  ██████╔╝██║     █████╗
    ██╔═══╝   ╚██╔╝  ██╔══╝  ██║   ██║██║╚██╗██║██║     ██╔══╝  ██╔══██╗██║     ██╔══╝
    ██║        ██║   ██║     ╚██████╔╝██║ ╚████║╚██████╗███████╗██████╔╝███████╗███████╗
    ╚═╝        ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═════╝ ╚══════╝╚══════╝

This submodule will provide the IANA logic and interface.

Author:
    Nissar Chababy, @funilrys, contactTATAfunilrysTODTODcom

Special thanks:
    https://pyfunceble.readthedocs.io/en/master/special-thanks.html

Contributors:
    http://pyfunceble.readthedocs.io/en/master/special-thanks.html

Project link:
    https://github.com/funilrys/PyFunceble

Project documentation:
    https://pyfunceble.readthedocs.io/en/master/

Project homepage:
    https://funilrys.github.io/PyFunceble/

License:
::


    MIT License

    Copyright (c) 2017-2019 Nissar Chababy

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""
# pylint: enable=line-too-long
# pylint: disable=bad-continuation
import PyFunceble
from PyFunceble.helpers import Dict, Download, File, Regex
from PyFunceble.lookup import Lookup


class IANA:  # pragma: no cover pylint: disable=too-few-public-methods
    """
    Logic behind the update and usage of `iana-domains-db.json`
    """

    def __init__(self):
        # We get the destination of the constructed IANA database.
        self.destination = (
            PyFunceble.CURRENT_DIRECTORY + PyFunceble.OUTPUTS["default_files"]["iana"]
        )

        if PyFunceble.path.isfile(self.destination):
            # The destination exist.

            # We get its content.
            self.iana_db = Dict().from_json(File(self.destination).read())
        else:
            # The destination does not exist.

            # We initiate the local variable which will save the content of the database.
            self.iana_db = {}

        # We initiate the URL to the IANA Root Zone Database page.
        self.iana_url = "https://www.iana.org/domains/root/db"

        # We iniitate an instance of Lookup.
        self.lookup = Lookup()

        # We map the list of server which have to be set manually because
        # they are not present into the IANA Root Zone Database.
        self.manual_server = {
            "aaa": "whois.nic.aaa",
            "abb": "whois.nic.abb",
            "able": "whois.nic.able",
            "accenture": "whois.nic.accenture",
            "aetna": "whois.nic.aetna",
            "aig": "whois.nic.aig",
            "americanexpress": "whois.nic.americanexpress",
            "amex": "whois.nic.amex",
            "amica": "whois.nic.amica",
            "amsterdam": "whois.nic.amsterdam",
            "analytics": "whois.nic.analytics",
            "aramco": "whois.nic.aramco",
            "arte": "whois.nic.arte",
            "as": "whois.nic.as",
            "athleta": "whois.nic.athleta",
            "audible": "whois.nic.audible",
            "author": "whois.nic.author",
            "aws": "whois.nic.aws",
            "axa": "whois.nic.axa",
            "azure": "whois.nic.azure",
            "baby": "whois.nic.baby",
            "banamex": "whois.nic.banamex",
            "bananarepublic": "whois.nic.bananarepublic",
            "baseball": "whois.nic.baseball",
            "bharti": "whois.nic.bharti",
            "bing": "whois.nic.bing",
            "bloomberg": "whois.nic.bloomberg",
            "bm": "whois.afilias-srs.net",
            "book": "whois.nic.book",
            "booking": "whois.nic.booking",
            "bot": "whois.nic.bot",
            "buzz": "whois.nic.buzz",
            "bz": "whois.afilias-grs.net",
            "call": "whois.nic.call",
            "calvinklein": "whois.nic.calvinklein",
            "caravan": "whois.nic.caravan",
            "cartier": "whois.nic.cartier",
            "caseih": "whois.nic.caseih",
            "cbn": "whois.nic.cbn",
            "cbre": "whois.nic.cbre",
            "cd": "chois.nic.cd",
            "chase": "whois.nic.chase",
            "circle": "whois.nic.circle",
            "cisco": "whois.nic.cisco",
            "citadel": "whois.nic.citadel",
            "citi": "whois.nic.citi",
            "citic": "whois.nic.citic",
            "cm": "whois.netcom.cm",
            "coupon": "whois.nic.coupon",
            "crown": "whois.nic.crown",
            "crs": "whois.nic.crs",
            "deal": "whois.nic.deal",
            "dealer": "whois.nic.dealer",
            "dell": "whois.nic.dell",
            "dhl": "whois.nic.dhl",
            "discover": "whois.nic.discover",
            "dnp": "whois.nic.dnp",
            "doosan": "whois.nic.doosan",
            "duns": "whois.nic.duns",
            "dupont": "whois.nic.dupont",
            "earth": "whois.nic.earth",
            "energy": "whois.nic.energy",
            "epost": "whois.nic.epost",
            "everbank": "whois.nic.everbank",
            "farmers": "whois.nic.farmers",
            "fast": "whois.nic.fast",
            "ferrero": "whois.nic.ferrero",
            "fire": "whois.nic.fire",
            "fj": "whois.usp.ac.fj",
            "flickr": "whois.nic.flickr",
            "flir": "whois.nic.flir",
            "food": "whois.nic.food",
            "ford": "whois.nic.ford",
            "fox": "whois.nic.fox",
            "free": "whois.nic.free",
            "frontier": "whois.nic.frontier",
            "ftr": "whois.nic.ftr",
            "ga": "whois.my.ga",
            "gap": "whois.nic.gap",
            "gh": "whois.nic.gh",
            "gmo": "whois.nic.gmo",
            "got": "whois.nic.got",
            "grainger": "whois.nic.grainger",
            "grocery": "whois.nic.grocery",
            "guardian": "whois.nic.guardian",
            "gucci": "whois.nic.gucci",
            "hair": "whois.nic.hair",
            "hbo": "whois.nic.hbo",
            "health": "whois.nic.health",
            "homegoods": "whois.nic.homegoods",
            "homesense": "whois.nic.homesense",
            "honeywell": "whois.nic.honeywell",
            "hot": "whois.nic.hot",
            "hoteles": "whois.nic.hoteles",
            "hotels": "whois.nic.hotels",
            "hotmail": "whois.nic.hotmail",
            "hsbc": "whois.nic.hsbc",
            "htc": "whois.nic.htc",
            "hyatt": "whois.nic.hyatt",
            "ieee": "whois.nic.ieee",
            "iinet": "whois.nic.iinet",
            "imdb": "whois.nic.imdb",
            "int": "whois.iana.org",
            "intel": "whois.nic.intel",
            "intuit": "whois.nic.intuit",
            "ipiranga": " whois.nic.ipiranga",
            "ipirange": "whois.nic.ipiranga",
            "itau": "whois.nic.itau",
            "iwc": "whois.nic.iwc",
            "jetzt": "whois.nic.jetzt",
            "jlc": "whois.nic.jlc",
            "jmp": "whois.nic.jmp",
            "jnj": "whois.nic.jnj",
            "jot": "whois.nic.jot",
            "joy": "whois.nic.joy",
            "jpmorgan": "whois.nic.jpmorgan",
            "jprs": "whois.nic.jprs",
            "kinder": "whois.nic.kinder",
            "kindle": "whois.nic.kindle",
            "kpmg": "whois.nic.kpmg",
            "kpn": "whois.nic.kpn",
            "kred": "whois.nic.kred",
            "kw": "whois.nic.kw",
            "lanxess": "whois.nic.lanxess",
            "lc": "whois2.afilias-grs.net",
            "lifeinsurance": "whois.nic.lifeinsurance",
            "like": "whois.nic.like",
            "lilly": "whois.nic.lilly",
            "lincoln": "whois.nic.lincoln",
            "living": "whois.nic.living",
            "lk": "whois.nic.lk",
            "loft": "whois.nic.loft",
            "lupin": "whois.nic.lupin",
            "maif": "whois.nic.maif",
            "marshalls": "whois.nic.marshalls",
            "mattel": "whois.nic.mattel",
            "mcd": "whois.nic.mcd",
            "mcdonalds": "whois.nic.mcdonalds",
            "merckmsd": "whois.nic.merckmsd",
            "microsoft": "whois.nic.microsoft",
            "mint": "whois.nic.mint",
            "mlb": "whois.nic.mlb",
            "mobily": "whois.nic.mobily",
            "moi": "whois.nic.moi",
            "montblanc": "whois.nic.montblanc",
            "moto": "whois.nic.moto",
            "msd": "whois.nic.msd",
            "mtpc": "whois.nic.mtpc",
            "mutual": "whois.nic.mutual",
            "mutuelle": "whois.nic.mutuelle",
            "nagoya": "whois.nic.nagoya",
            "nba": "whois.nic.nba",
            "netflix": "whois.nic.netflix",
            "neustar": "whois.nic.neustar",
            "nfl": "whois.nic.nfl",
            "nhk": "whois.nic.nhk",
            "nike": "whois.nic.nike",
            "northwesternmutual": "whois.nic.northwesternmutual",
            "now": " whois.nic.now",
            "ntt": "whois.nic.ntt",
            "nyc": "whois.nic.nyc",
            "office": "whois.nic.office",
            "okinawa": "whois.nic.okinawa",
            "oldnavy": "whois.nic.oldnavy",
            "open": "whois.nic.open",
            "orientexpress": "whois.nic.orientexpress",
            "otsuka": "whois.nic.otsuka",
            "passagens": "whois.nic.passagens",
            "pay": "whois.nic.pay",
            "pfizer": "whois.nic.pfizer",
            "pharmacy": " whois.nic.pharmacy",
            "piaget": " whois.nic.piaget",
            "pictet": "whois.nic.pictet",
            "pin": "whois.nic.pin",
            "ping": "whois.nic.ping",
            "pramerica": "whois.nic.pramerica",
            "praxi": "whois.nic.praxi",
            "prime": "whois.nic.prime",
            "pru": "whois.nic.pru",
            "prudential": "whois.nic.prudential",
            "ps": "whois.pnina.ps",
            "qvc": "whois.nic.qvc",
            "read": "whois.nic.read",
            "realtor": "whois.nic.realtor",
            "ren": "whois.nic.ren",
            "rocher": "whois.nic.rocher",
            "room": "whois.nic.room",
            "rw": "whois.ricta.org.rw",
            "ryukyu": "whois.nic.ryukyu",
            "safe": "whois.nic.safe",
            "safety": "whois.nic.safety",
            "sakura": "whois.nic.sakura",
            "sapo": "whois.nic.sapo",
            "sas": "whois.nic.sas",
            "save": "whois.nic.save",
            "secure": "whois.nic.secure",
            "sener": "whois.nic.sener",
            "shaw": "whois.afilias-srs.net",
            "shop": "whois.nic.shop",
            "silk": "whois.nic.silk",
            "skype": "whois.nic.skype",
            "sl": "whois.nic.sl",
            "smile": "whois.nic.smile",
            "sohu": "whois.nic.sohu",
            "song": "whois.nic.song",
            "spot": "whois.nic.spot",
            "staples": "whois.nic.staples",
            "statefarm": "whois.nic.statefarm",
            "stream": "whois.nic.stream",
            "suzuki": "whois.nic.suzuki",
            "swiftcover": "whois.nic.swiftcover",
            "talk": "whois.nic.talk",
            "taobao": "whois.nic.taobao",
            "target": "whois.nic.target",
            "tjmaxx": "whois.nic.tjmaxx",
            "tjx": "whois.nic.tjx",
            "tkmaxx": "whois.nic.tkmaxx",
            "tmall": "whois.nic.tmall",
            "tokyo": "whois.nic.tokyo",
            "tube": "whois.nic.tube",
            "tunes": "whois.nic.tunes",
            "tushu": "whois.nic.tushu",
            "tvs": "whois.nic.tvs",
            "unicom": "whois.nic.unicom",
            "uno": "whois.nic.uno",
            "vivo": "whois.nic.vivo",
            "vuelos": "whois.nic.vuelos",
            "wanggou": "whois.nic.wanggou",
            "watches": "whois.nic.watches",
            "weather": "whois.nic.weather",
            "weatherchannel": "whois.nic.weatherchannel",
            "weir": "whois.nic.weir",
            "whois": "whois.nic.qpon",
            "windows": "whois.nic.windows",
            "winners": "whois.nic.winners",
            "wow": "whois.nic.wow",
            "xbox": "whois.nic.xbox",
            "xn--1ck2e1b": "whois.nic.xn--1ck2e1b",
            "xn--2scrj9c": "whois.inregistry.net",
            "xn--3hcrj9c": "whois.inregistry.net",
            "xn--45br5cyl": "whois.inregistry.net",
            "xn--45brj9c": "whois.inregistry.net",
            "xn--8y0a063a": "whois.nic.xn--8y0a063a",
            "xn--bck1b9a5dre4c": "whois.nic.xn--bck1b9a5dre4c",
            "xn--cck2b3b": "whois.nic.xn--cck2b3b",
            "xn--czr694b": "whois.nic.xn--czr694b",
            "xn--e1a4c": "whois.eu",
            "xn--eckvdtc9d": "whois.nic.xn--eckvdtc9d",
            "xn--fct429k": "whois.nic.xn--fct429k",
            "xn--fpcrj9c3d": "whois.inregistry.net",
            "xn--fzc2c9e2c": "whois.nic.lk",
            "xn--g2xx48c": "whois.nic.xn--g2xx48c",
            "xn--gckr3f0f": "whois.nic.xn--gckr3f0f",
            "xn--gecrj9c": "whois.inregistry.net",
            "xn--gk3at1e": "whois.nic.xn--gk3at1e",
            "xn--h2breg3eve": "whois.inregistry.net",
            "xn--h2brj9c": "whois.inregistry.net",
            "xn--h2brj9c8c": "whois.inregistry.net",
            "xn--imr513n": "whois.nic.xn--imr513n",
            "xn--jvr189m": "whois.nic.xn--jvr189m",
            "xn--kpu716f": "whois.nic.xn--kpu716f",
            "xn--mgba3a3ejt": "whois.nic.xn--mgba3a3ejt",
            "xn--mgbb9fbpob": "whois.nic.xn--mgbb9fbpob",
            "xn--mgbbh1a": "whois.inregistry.net",
            "xn--mgbbh1a71e": "whois.inregistry.net",
            "xn--mgbgu82a": "whois.inregistry.net",
            "xn--nyqy26a": "whois.nic.xn--nyqy26a",
            "xn--otu796d": "whois.nic.xn--otu796d",
            "xn--pbt977c": "whois.nic.xn--pbt977c",
            "xn--rhqv96g": "whois.nic.xn--rhqv96g",
            "xn--rovu88b": "whois.nic.xn--rovu88b",
            "xn--rvc1e0am3e": "whois.inregistry.net",
            "xn--s9brj9c": "whois.inregistry.net",
            "xn--ses554g": "whois.registry.knet.cn",
            "xn--wgbh1c": "whois.dotmasr.eg",
            "xn--xkc2al3hye2a": "whois.nic.lk",
            "xn--xkc2dl3a5ee0h": "whois.inregistry.net",
            "yahoo": "whois.nic.yahoo",
            "yamaxun": "whois.nic.yamaxun",
            "yandex": "whois.nic.yandex",
            "yokohama": "whois.nic.yokohama",
            "you": "whois.nic.you",
            "za": "whois.registry.net.za",
            "zappos": "whois.nic.zappos",
            "zero": "whois.nic.zero",
            "zippo": "whois.nic.zippo",
        }

    def load(self):
        """
        Initiate the IANA database if it is not the case.
        """

        if "iana_db" not in PyFunceble.INTERN or not PyFunceble.INTERN["iana_db"]:
            # The global database is empty, None or does not exist.

            # We update it with the database content.
            PyFunceble.INTERN["iana_db"] = self.iana_db

    def _referer(self, extension):
        """
        Return the referer for the given extension.

        :param extension: A valid domain extension.
        :type extension: str

        :return: The whois server to use to get the WHOIS record.
        :rtype: str
        """

        # We get the a copy of the page.
        iana_record = self.lookup.whois(
            PyFunceble.CONFIGURATION["iana_whois_server"], "hello.%s" % extension
        )

        if iana_record and "refer" in iana_record:
            # The record is not empty.

            # We initiate a regex which will extract the referer.
            regex_referer = r"(?s)refer\:\s+([a-zA-Z0-9._-]+)\n"

            # We try to extract the referer.
            matched = Regex(
                iana_record, regex_referer, return_data=True, group=1
            ).match()

            if matched:
                # The referer was extracted successfully.

                # We return the matched referer.
                return matched

        # * The referer was not extracted successfully.
        # or
        # * The iana record is empty.

        if extension in self.manual_server:
            # The extension is in the list of manual entries.

            # We return the server which we set manually.
            return self.manual_server[extension]

        # We return None because we weren't able to get the server to call for
        # the given extension.
        return None

    def _extensions(self):
        """
        Extract the extention from the given block.
        Plus get its referer.
        """

        upstream_lines = (
            Download(self.iana_url, return_data=True)
            .text()
            .split('<span class="domain tld">')
        )

        # We extract the different extension from the currently readed line.
        regex_valid_extension = r"(/domains/root/db/)(.*)(\.html)"

        for block in upstream_lines:
            if "/domains/root/db/" in block:
                # The link is in the line.

                # We try to extract the extension.
                matched = Regex(
                    block, regex_valid_extension, return_data=True, rematch=True
                ).match()[1]

                if matched:
                    # The extraction is not empty or None.

                    # We get the referer.
                    referer = self._referer(matched)

                    # We yield the matched extension and its referer.
                    yield (matched, referer)

    def update(self):
        """
        Update the content of the `iana-domains-db` file.
        """

        if not PyFunceble.CONFIGURATION["quiet"]:
            # * The quiet mode is not activated.

            # We print on screen what we are doing.
            print("Update of iana-domains-db", end=" ")

        # We loop through the line of the iana website.
        for extension, referer in self._extensions():

            if extension not in self.iana_db or self.iana_db[extension] != referer:
                # We add the extension to the databae.
                self.iana_db[extension] = referer

                # We save the content of the constructed database.
                Dict(self.iana_db).to_json(self.destination)

        if not PyFunceble.CONFIGURATION["quiet"]:
            # The quiet mode is not activated.

            # We indicate that the work is done without any issue.
            print(PyFunceble.INTERN["done"])
