Summary:	An interpreter for the awk programming language
Summary(de):	Mikes neuer Posix AWK-Interpretierer
Summary(es):	Nuevo interpretador (Posix) AWK del Mike
Summary(fr):	Mike's New/Posix AWK Interpreter : interpr�teur AWK
Summary(pl):	Interpreter j�zyka programowania awk
Summary(pt_BR):	Novo interpretador (Posix) AWK do Mike
Summary(tr):	Posix AWK Yorumlay�c�s�
Name:		mawk
Version:	1.3.3
Release:	21
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Source0:	ftp://ftp.whidbey.net/pub/brennan/%{name}%{version}.tar.gz
Source1:	%{name}.1.pl
Patch0:		%{name}-fix_%{name}_path.patch
Patch1:		%{name}-ac-workaround.patch
Provides:	/bin/awk
Provides:	awk
BuildRequires:	autoconf
%{?BOOT:BuildRequires:	glibc-static}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/

%description
Mawk is a version of the awk programming language. Awk interprets a
special-purpose programming language to do quick text pattern matching
and reformatting. Mawk improves on awk in certain ways and can
sometimes outperform gawk, the standard awk program for Linux. Mawk
conforms to the POSIX 1003.2 (draft 11.3) definition of awk.

%description -l de
Mawk ist eine Version von awk, einem leistungsf�higen
Textverarbeitungsprogramm. In bestimmten Bereichen leistet mawk mehr
als gawk, das Standard-awk-Programm auf Linux.

%description -l es
Mawk es una versi�n del awk, que es un fuerte programa procesador de
texto. En algunas �reas mawk puede superar gawk, que es el programa
awk padr�n del Linux.

%description -l fr
mawk est une version d'awk, un puissant programme de traitement du
texte. Dans certains cas, mawk peut �tre sup�rieur � gawk, qui est le
programme awk standard sur Linux

%description -l pl
Mawk jest wersj� interpretera j�zyka programowania awk. Awk jest
specjalizowanym j�zykiem programowania do szybkiego przetwarzania
tekst�w. Mawk w pewien spos�b ulepsza awk i czasem przerasta nawet
gawk - standardowy interpreter awk-a w Linuksie. Mawk jest zgodny ze
standardem j�zyka awk opisanym w POSIX 1003.2 (draft 11.3).

%description -l pt_BR
Mawk � uma vers�o do awk, que � um poderoso programa processador de
texto. Em algumas �reas mawk pode superar gawk, que � o programa awk
padr�o do Linux.

%description -l tr
Mawk, �ok g��l� bir metin i�leme program� olan awk'�n bir s�r�m�d�r.
Baz� durumlarda Linux un standart awk program� olan gawk'dan daha
�st�nd�r.

%package BOOT
Summary:	An interpreter for the awk programming language - BOOT
Summary(de):	Mikes neuer Posix AWK-Interpretierer - BOOT
Summary(fr):	Mike's New/Posix AWK Interpreter : interpr�teur AWK - BOOT
Summary(pl):	Interpreter j�zyka programowania awk - BOOT
Summary(tr):	Posix AWK Yorumlay�c�s� - BOOT
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst

%description BOOT
Bootdisk awk version.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf
%configure
%if %{?BOOT:1}%{!?BOOT:0}
%{__make} MATHLIB=/usr/lib/libm.a
mv -f mawk mawk.BOOT
%{__make} clean
%endif
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{man1,pl/man1},%{_examplesdir}/%{name},/bin}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	BINDIR=$RPM_BUILD_ROOT%{_bindir}

ln -sf mawk $RPM_BUILD_ROOT%{_bindir}/awk
echo ".so mawk.1" > $RPM_BUILD_ROOT%{_mandir}/man1/awk.1

install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1/mawk.1
echo ".so mawk.1" > $RPM_BUILD_ROOT%{_mandir}/pl/man1/awk.1

mv -f examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%if %{?BOOT:1}%{!?BOOT:0}
install -d $RPM_BUILD_ROOT/usr/lib/bootdisk/bin
install mawk.BOOT $RPM_BUILD_ROOT/usr/lib/bootdisk/bin/awk
%endif

gzip -9nf ACKNOWLEDGMENT CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/mawk
%attr(755,root,root) /bin/awk
%{_examplesdir}/%{name}
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%if %{?BOOT:1}%{!?BOOT:0}
%files BOOT
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/bootdisk/bin/awk
%endif
