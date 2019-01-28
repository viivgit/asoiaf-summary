# asoiaf-summary #

Creates a summary of the 5 first novels of A Song of Ice and Fire (ASOIAF) from the summaries of each chapter available on the [**wiki of A World of Ice and Fire (AWOIAF)**](https://awoiaf.westeros.org) in EPUB, AZW3 (Kindle), MOBI, and PDF formats.
Novels included so far are:
* A Game of Thrones
* A Clash of Kings
* A Storm of Swords
* A Feast for Crows
* A Dance with Dragons

The final products, i.e. the eBooks and the PDF, are not included here, this is just the code used to make them.
To download them, see the last available release I posted [**here**](https://www.reddit.com/r/asoiaf/comments/8zki6e/spoilers_main_update_v11_ebookpdf_summary_of_all/) on Reddit .

# Notes #
The code so far just works on Windows, but for any UNIX system, you just need to replace the `.bat` file with a shell file that fits your system, it should be pretty straightforward.

The rest of the code is in Python so there is no compatibility problem.

Since a part of the code uses my modified version of [**Pypub**](https://github.com/wcember/pypub) (included in the `pypubmod` folder), which runs in Python 2, **you need to have both Python 2 and Python 3 installed**.

You also **need to have [**Calibre**](https://calibre-ebook.com/) installed** to convert to other formats than Epub.

**IMPORTANT:** This code downloads data from AWOIAF (about 350 HTML pages) each time it is run, and even though it is only a couple MB large, doing so repeatedly _is not advised_.

Once again, if you just want the final product (the eBooks, or the PDF), refer to the Reddit [**page**](https://www.reddit.com/r/asoiaf/comments/akq4vd/spoilers_main_update_v12_ebookpdf_summary_of_all/), since they are not contained here.

The purpose of this code is just to show how it is done to anyone interested, ideally it should only be run once every few months, since the data on the Wiki is unlikely to change drastically in short time frames, and the final products are already  pretty complete as of early 2019.

**LICENSE OF THE OUTPUT FILES:** The output files are all under the [**CC-BY-SA 3.0**](https://creativecommons.org/licenses/by-sa/3.0/) license, as indicated on the Credits page inside each of them.

# Quickstart #
Run `script_to_run.bat`. That is all, there is nothing else to do.

It will:
* download the HTML files necessary (and only them)
* clean them so that only the text remains, and a few other pieces of information such as a small Navigation section, and the places where the chapter takes place
* build an Epub with a cover and Table of Contents out of the cleaned files
* convert that Epub to AZW3 (for Kindle), MOBI (for older e-readers not supporting Epub), and PDF
* the files produced will appear in the folder where you downloaded the code with the file name `asoiaf-summary` and their respective extensions

# Configuration #
Actually, even on Windows, depending on your installation, you might have to change the `script_to_run.bat` file.

It is currently configured to use the syntax `py -2` and `py -3` to start Python 2 and 3 respectively, but this will only work if you installed Python from the official [**page**](https://www.python.org/downloads/windows/). See this [**page**](https://docs.python.org/3/using/windows.html#getting-started) for information on this syntax.

Otherwise (if you have an Anaconda distribution for instance) you can just replace in the `.bat` file the `py -2` and `py -3` commands with the full path to your Python 2 and 3 executables, and you are done.

# Copyright and License #

Copyright (c) 2019 viivgit

[**Licensed**](https://github.com/viivgit/asoiaf-summary/blob/master/LICENSE) under the MIT License.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
