using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class coin : MonoBehaviour
{
    // Start is called before the first frame update
    private void onCollisonEnter(Collison collison)
    {
        Destroy (gameObject);
    // Update is called once per frame
    }
}
