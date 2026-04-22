# LeetCode 75 - Python Solutions

Solutions to the curated [LeetCode 75](https://leetcode.com/studyplan/leetcode-75/) problem list in Python 3.

**Progress:** 39 / 75

**Live site:** [ariana0505.github.io/leetcode75-python](https://ariana0505.github.io/leetcode75-python) — browse problems with syntax-highlighted code, bilingual statements (EN/ES), and keyboard navigation.

## Problems

### Array & Hashing

| #  | Problem | Solution |
|----|---------|----------|
| 01 | Two Sum | [two_sum.py](01-two-sum/) |
| 03 | Contains Duplicate | [contains_duplicate.py](03-contains-duplicate/) |
| 04 | Product of Array Except Self | [product_of_array.py](04-product-of-Array-Except-Self/) |
| 30 | Longest Consecutive Sequence | [longest_consecutive.py](30-longest-consecutive-sequence/) |
| 52 | Group Anagrams | [group_anagrams.py](52-group-anagrams/) |
| 72 | Top K Frequent Elements | [top_k_frequent.py](72-top-k-frequent-elements/) |
| 74 | Valid Anagram | [valid_anagram.py](74-valid-Anagram/) |
| 57 | Encode and Decode String | [encode_decode.py](57-encode-and-decode-string/) |

### Two Pointers

| #  | Problem | Solution |
|----|---------|----------|
| 09 | 3Sum | [three_sum.py](09-3Sum/) |
| 10 | Container With Most Water | [container_water.py](10-conteiner-most_water/) |

### Sliding Window

| #  | Problem | Solution |
|----|---------|----------|
| 02 | Best Time to Buy and Sell Stock | [buy_sell_stock.py](02-best-time-to-buy-and-sell-stock/) |
| 49 | Longest Substring Without Repeating Characters | [longest_substring.py](49-longest-substring-without-repeating-characters/) |
| 50 | Longest Repeating Character Replacement | [longest_repeating.py](50-longest-repeating-character-replacement/) |
| 51 | Minimum Window Substring | [min_window.py](51-minimum-window-substring/) |

### Binary Search

| #  | Problem | Solution |
|----|---------|----------|
| 07 | Find Minimum in Rotated Sorted Array | [find_minimum.py](07-find-minimum-in-rotated-sorted-array/) |
| 08 | Search in Rotated Sorted Array | [search_rotated.py](08-search-in-rotated-sorted-array/) |

### Linked List

| #  | Problem | Solution |
|----|---------|----------|
| 40 | Linked List Cycle | [linked_list_cycle.py](40-linked-list-cycle/) |
| 41 | Merge Two Sorted Lists | [merge_lists.py](41-merge-two-sorted-lists/) |

### Tree

| #  | Problem | Solution |
|----|---------|----------|
| 59 | Same Tree | [same_tree.py](59-same-tree/) |
| 60 | Invert Binary Tree | [invert_tree.py](60-invert-binary-tree/) |
| 64 | Subtree of Another Tree | [subtree.py](64-subtree-of-another-tree/) |
| 66 | Validate Binary Search Tree | [validate_bst.py](66-validate-binary-search-tree/) |

### Dynamic Programming

| #  | Problem | Solution |
|----|---------|----------|
| 05 | Maximum Subarray | [max_subarray.py](05-maximum-subarray/) |
| 06 | Maximum Product Subarray | [max_product.py](06-Maximum-product-subarray/) |
| 15 | Climbing Stairs | [climbing_stairs.py](15-climbing-stairs/) |
| 16 | Coin Change | [coin_change.py](16-coin-change/) |
| 17 | Longest Increasing Subsequence | [lis.py](17-longest-increasing-subsequence/) |
| 19 | Word Break | [word_break.py](19-word-break/) |
| 20 | Combination Sum | [combination_sum.py](20-combination-sum/) |
| 21 | House Robber & House Robber II | [house_robber.py](21-house-robber-and-2/) |
| 22 | Longest Palindromic Substring | [longest_palindromic_substring.py](22-longest-palindromic-substring/) |

### Bit Manipulation

| #  | Problem | Solution |
|----|---------|----------|
| 11 | Number of 1 Bits | [number_1_bits.py](11-number-1-bits/) |
| 12 | Counting Bits | [counting_bits.py](12-counting-bits/) |
| 13 | Missing Number | [missing_number.py](13-missing-number/) |
| 14 | Reverse Bits | [reverse_bits.py](14-reverse-bits/) |
| 75 | Sum of Two Integers | [sum_two_int.py](75-sum-of-two-integer/) |

### Intervals

| #  | Problem | Solution |
|----|---------|----------|
| 34 | Insert Interval | [insert_interval.py](34-insert-interval/) |
| 35 | Merge Intervals | [merge_intervals.py](35-merge-intervals/) |
| 37 | Meeting Rooms | [meeting_rooms.py](37-meeting-rooms/) |

## How to Run

```bash
python3 01-two-sum/two_sum.py
```

Each solution is a standalone script with inline test cases.

## Site

The companion website is built with [Astro](https://astro.build/) and lives in the [`site/`](site/) directory. It reads directly from the solution files and `statement.md` in each problem directory.

```bash
cd site
npm install
npm run dev      # local dev server at localhost:4321
npm run build    # static build to site/dist/
```

**Features:** dark terminal theme, syntax-highlighted Python code, bilingual problem statements (EN/ES), keyboard shortcuts (`h`/`l` or arrows to navigate, `?` for help).

Deployed automatically to GitHub Pages via GitHub Actions on push to `main`.
