%global tl_name ndsu-thesis-2022
%global tl_revision 63881

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	North Dakota State University disquisition class 2022
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ndsu-thesis-2022
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ndsu-thesis-2022.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ndsu-thesis-2022.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A class for generating disquisitions (MS and PhD - thesis, dissertation,
and paper), intended to be in compliance with North Dakota State
University requirements. Updated (2022) North Dakota State University
LaTeX thesis class features several functionalities, including not
limited to, numbered and non-numbered versions, overall justification,
document point sizes, fonts options, SI units, show frames, URL
breaking, long tables, subfigures, multi-page figures, chapter styles,
subfiles, algorithm listing, BibTeX and BibLaTeX support, individual
chapter and whole document bibliography, natbib citations, and clever
references. The supplied simple and extended samples illustrate these
features and guide students to use the class.

