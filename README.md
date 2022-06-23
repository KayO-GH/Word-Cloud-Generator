# Word Cloud Generator
A simple way to generate word clouds from PDFs, Word Documents, and text-based files.

[Open in Google Colab](https://githubtocolab.com/KayO-GH/Word-Cloud-Generator/blob/main/read_files_to_wordcloud.ipynb) and save a copy to use.  
**Note:** The Colab notebook runs best with **Google Chrome**.

---

#### Scenarios:
1. Single file -> Single word cloud
2. Multiple files -> Single word cloud
3. Multiple files -> Multiple word clouds + Combined word cloud

#### Instructions (for running in [Colab](https://githubtocolab.com/KayO-GH/Word-Cloud-Generator/blob/main/read_files_to_wordcloud.ipynb)):
1. Run the entire file: From the menu, select `Runtime` then `Run all`
2. Click on the `Upload Files` button to upload your files
3. Set the appropriate parameters by toggling the **Yes/No** buttons in the "Settings" cell.
4. Click `Run` and wait for the word clouds to be generated. Wait till you see the message **### Done ###** in the cell logs, or a wordcloud with the title **"Combined Word Cloud"**.
5. Click `Download` to get a zip file of your word cloud images.

#### Limitations:
* Text in images cannot be read. Here is a [workaround](https://www.thewindowsclub.com/extract-text-from-an-image-in-word) to extract text from images.
* Scanned PDFs _(You know a PDF was scanned if you can't select text with your mouse when you open it normally)_
    * SOTA OCR methods are still not perfect
    * OCR text recognition takes longer to run
    * \*Key takeaway: If you can get a machine-generated PDF, use that, else tag your **scanned PDF** files properly by renaming them to end with `_scanned.pdf`

#### Known Issues:
* Sometimes, the required packages fail to install correctly, leading to an error in the logs that says: `ERROR: module 'PIL.Image' has no attribute 'Transpose'`. In this scenario, go to `Runtime` in the menu, and select `Restart and run all`. This should fix the problem, and you can go through the steps outlined in the instructions.
* Upoading files using the Firefox browser has been known to go a bit wonky. This is an erratic bug in Colab itself. For the best experience, use Google Chrome.
