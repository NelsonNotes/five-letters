import { TAttemptInput, TAttemptResponse } from "../types/attempt";

// A mock function to mimic making an async request for data
export const attemptAPI = {
  postAttempt: (attempt: TAttemptInput) => {
    return new Promise<TAttemptResponse>((resolve) =>
      setTimeout(
        () =>
          resolve({
            attempt: attempt.attempt,
            letters_status: [2, 1, 1, 0, 0],
          }),
        500
      )
    );
  },
};
