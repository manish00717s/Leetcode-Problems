/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays=(a,b)=>(c=[...a,...b].sort((x,y)=>x-y),n=c.length,n%2?c[n>>1]:(c[n/2-1]+c[n/2])/2)
