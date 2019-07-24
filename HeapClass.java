import java.util.*;

class HeapClass
{
  private int heap[];
  private int size;
  private int max_size;

  HeapClass(int max_size)
  {
    this.max_size = max_size;
    heap = new int[this.max_size+1];
    this.size = 0;
    heap[0] = Integer.MAX_VALUE;
  }
  void swap(int a, int b)
  {
    int temp;
    temp = heap[a];
    heap[a] = heap[b];
    heap[b] = temp;
  }

  public void insert(int val)
  {
    if(size == max_size)
    {
      System.out.println("the heap is full");
    }
    else
    {
      heap[++size] = val;
      int cur = size;
      while(heap[cur] > heap[(cur)/2])
      {
        swap(cur, (cur)/2);
        cur = (cur)/2;
      }
    }
  }

  private boolean isLeaf(int pos)
	{
		if (pos >= (size / 2) && pos <= size) {
			return true;
		}
		return false;
	}

  public void heapify(int pos)
  {
    if (isLeaf(pos))
			return;

    if(heap[pos] < heap[pos*2] || heap[pos] < heap[pos*2+1])
    {
      if(heap[pos*2] > heap[pos*2+1])
      {
        swap(pos*2, pos);
        heapify(pos*2);
      }
      else
      {
        swap(pos*2+1, pos);
        heapify(pos*2+1);
      }
    }
  }

  public void extractMax()
  {
    int max_val = heap[1];
    heap[1] = heap[this.size--];
    heapify(1);
  }

  public void print()
    {
        for (int i = 1; i <= ((size)/2); i++)
        {
            System.out.print(" PARENT : " + heap[i] + " LEFT CHILD : " + heap[2 * i] + " RIGHT CHILD :" + heap[(2 * i) + 1]);
            System.out.println();
        }
    }

  public static void main(String[]qw)
  {
    HeapClass maxHeap = new HeapClass(15);
    maxHeap.insert(5);
        maxHeap.insert(3);
        maxHeap.insert(17);
        maxHeap.insert(10);
        maxHeap.insert(84);
        maxHeap.insert(19);
        maxHeap.insert(6);
        maxHeap.insert(22);
        maxHeap.insert(9);
        maxHeap.print();
        for(int i = 1; i <= maxHeap.size; i++)
        {
          System.out.println(maxHeap.heap[i]);
        }
  }
}
