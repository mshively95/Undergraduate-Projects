using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class WebSave : MonoBehaviour 
{
	public GameObject cube;
	public GameObject cube1;
	
	string str = "cubeposition";
	//string str1 = "cubeposition1";//
	

	public void Save()
	{	
		
	
		/* Vector3 cubepos = cube.transform.position;
		Vector3 cubepos1 = cube1.transform.position;
		
		ES2.Save(cubepos, str);
		
		ES2.Save(cubepos1, str1); */
		
		ES2.Save(SceneManager.GetActiveScene().name, "SavedScene");
		
		StartCoroutine("UploadMesh");
	}
	
	public IEnumerator UploadMesh()
{
	Vector3 cubepos = cube.transform.position;
	
    // Create a URL and add parameters to the end of it.
    string myURL = "http://cgi.soic.indiana.edu/~team05/ES2.php";
    myURL += "?webfilename=" + str + "&webusername=tsajnani&webpassword=Capstone2017";
 
    // Create our ES2Web object.
    ES2Web web = new ES2Web(myURL + "&tag=tag");
      
    // Start uploading our data and wait for it to finish.
    yield return StartCoroutine(web.Upload(cubepos));
      
    if(web.isError)
    {
        // Enter your own code to handle errors here.
        Debug.LogError(web.errorCode + ":" + web.error);
    }
	
	//Debug.Log("done");
}
}