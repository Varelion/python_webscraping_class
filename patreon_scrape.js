// This code is to be ran on the console of a patreon store.

// We scrape for what we want

let x = document.getElementsByTagName('a')

// Create the object that will become the JSON we will use.
let files = {

}


// --------------------------
//#region SCRAPING FOR A TAGS
// --------------------------
// for (let i = 0; i < x.length; i++) {
// 	// Check if the text content of the <a> element contains "click here"
// 	if (x[i].text == 'JSON') {
// 		// Do something with the matching element, if needed
// 		// We define the parent node of where the x is situated. Then we remove what will be extracted from teh string
// 		let textAfterJSON = x[i].parentNode.textContent.split(" JSON | ZIP")
// 		// We save to itself what is left after the split / extraction
// 		textAfterJSON = textAfterJSON[0]
// 		// We then create entries for the files object, with the name of the parent object, and the value of the link
// 		files[textAfterJSON] = x[i].href
// 	}
// }
// console.log(files)

//#endregion SCRAPING FOR A TAGS

for (let i = 0; i < x.length; i++) {
	// Check if the text content of the <a> element contains "click here"
	if (x[i].href.includes('dropbox')) {
		let link = x[i].href

		// Do something with the matching element, if needed
		// We define the parent node of where the x is situated. Then we remove what will be extracted from teh string
		files[x[i].text] = link
		console.log(x[i].text)

	}
}

console.log(files)

// output can be found at './Cze_Peku_Animated_Maps_For_Foundry.json' OR './Cze_Peku_Foundry_VTT_Master_Post.json'
