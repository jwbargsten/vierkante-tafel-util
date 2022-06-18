# vierkante-tafel-util

Core functions to determine if a person or a group of persons should be selected for the
next turn. The goal is to distribute the turns for each person so that the group
selection and the number of turns per person is evenly distributed.


$$weight(p, G, H) = weightPerson(ndays(p \in H), ndraws(p, p \in H)) * \prod_{g \in G} weightPerson(ndays((p, g) \in H), ndraws((p, g) \in H))$$

## License

```
Copyright 2022 Joachim Bargsten

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
